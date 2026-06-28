from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField
from utils.schema_utils import type_map
import re
from pathlib import Path

years = [2021, 2022, 2023, 2024, 2025]

for year in years:

    path_schema = (Path.cwd().parent / "schemas" / f"landing_{year}.csv")
    
    # load schema definition
    df_schema = (
        spark.read.format("csv")
        .option("header", "true")
        .option("skipRows", 4)
        .load(f"file:{path_schema}")
    )

    # extract schema metadata
    schema_rows = (
        df_schema
        .select("Column Name", "Data Type", "Include")
        .collect()
    )

    # column list
    include_cols = [
        row["Column Name"]
        for row in schema_rows
        if row["Include"] == "Y"
    ]

    # spark schema
    spark_schema = StructType([
        StructField(
            row["Column Name"],
            type_map[row["Data Type"].strip().lower()],
            True
        )
        for row in schema_rows
    ])

    path_data = (
        f"abfss://stackoverflow@stackoverflowstorage.dfs.core.windows.net/"
        f"landing/results_{year}.csv"
    )

    # load source data
    df_data = (
        spark.read.format("csv")
        .option("header", "true")
        .option("multiLine", "true")
        # required: multiline free-text responses with embedded quotes
        .option("escape", '"')
        .schema(spark_schema)
        .load(path_data)
        .select(*include_cols)
        .withColumn("Year", F.lit(year))
    )

    # duplicate check
    dup_df = (
        df_data
        .groupBy("ResponseId")
        .count()
        .filter(F.col("count") > 1)
    )

    if dup_df.limit(1).count() > 0:
        print(f"WARNING: duplicates found in {year}")
        display(dup_df)

    # sanitize column names
    sanitized_cols = [
        re.sub(r"[ ,;{}()\n\t=]", "_", c)
        for c in df_data.columns
    ]

    df_data = df_data.toDF(*sanitized_cols)

    # save to bronze layer
    (
        df_data.write.format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .saveAsTable(f"stackoverflow.bronze.result_{year}")
    )
