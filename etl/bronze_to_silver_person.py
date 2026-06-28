from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField
from functools import reduce
import re
from pathlib import Path
from utils.schema_utils import type_map
from utils.clearning_functions import (
    build_contains_expr,
    build_exact_expr,
    build_startswith_expr,
    build_yearscode_expr
)
from utils.clearning_rules import (
    MainBranch_RULES,
    Edlevel_RULES,
    RemoteWork_RULES,
    PurchaseInfluence_RULES,
    NewRole_RULES,
    AISelect_RULES,
    AISent_RULES,
    AIAcc_RULES,
    Age_RULES,
    Industry_RULES,
    OrgSize_RULES,
    DevType_RULES,
    Employment_RULES
)

years = [2021, 2022, 2023, 2024, 2025]
df_all_years = []

contains_columns = [
    ("MainBranch", "MainBranch_Category", MainBranch_RULES),
    ("EdLevel", "EdLevel_Category", Edlevel_RULES),
    ("RemoteWork", "RemoteWork_Category", RemoteWork_RULES),
    ("PurchaseInfluence", "PurchaseInfluence_Category", PurchaseInfluence_RULES),    
    ("NewRole", "NewRole_Category", NewRole_RULES),
    ("AISelect", "AISelect_Category", AISelect_RULES),
    ("AISent", "AISent_Category", AISent_RULES),
    ("AIAcc", "AIAcc_Category", AIAcc_RULES),
]

exact_columns = [
    ("Age", "Age_Category", Age_RULES),
    ("Industry", "Industry_Category", Industry_RULES),
    ("OrgSize", "OrgSize_Category", OrgSize_RULES),
]

path_schema = (Path.cwd().parent / "schemas" / f"silver_person.csv")

for year in years:

    # load schema definition
    df_schema = (
        spark.read.format("csv")
        .option("header", "true")
        .option("skipRows", 5)
        .load(f"file:{path_schema}")
    )

    schema_rows = (
        df_schema
        .select("Column Name", "Data Type")
        .collect()
    )

    # spark schema
    schema_map = {
        r["Column Name"]: type_map[r["Data Type"].strip().lower()]
        for r in schema_rows
    }

    include_cols = list(schema_map.keys())

    # load bronze table
    path_table = f"stackoverflow.bronze.result_{year}"

    df = (
        spark.read.table(path_table)
        .replace("NA", None)
    )

    # contains match
    for source_col, target_col, rules in contains_columns:
        if source_col in df.columns:
            df = df.withColumn(
                target_col,
                build_contains_expr(source_col, rules)
            )
    
    # exact match
    for source_col, target_col, rules in exact_columns:
        if source_col in df.columns:
            df = df.withColumn(
                target_col,
                build_exact_expr(source_col, rules)
            )
        
    # special
    # DevType
    if "DevType" in df.columns:
        first_devtype = F.trim(
            F.split(F.col("DevType"), ";")[0]
        )

    df = df.withColumn(
        "DevType_Primary",
        first_devtype
    )

    df = df.withColumn(
        "DevType_Category",
        build_contains_expr(
            "DevType_Primary",
            DevType_RULES
        )
    )

    # Employment
    if "Employment" in df.columns:
        first_employment = F.trim(
            F.split(F.col("Employment"), ";")[0]
        )

    df = df.withColumn(
        "Employment_Primary",
        first_employment
    )

    df = df.withColumn(
        "Employment_Category",
        build_startswith_expr(
            "Employment_Primary",
            Employment_RULES
        )
    )

    # YearsCode
    if "YearsCode" in df.columns:
        df = df.withColumn(
            "YearsCode_Cleaned",
            build_yearscode_expr(
                "YearsCode"
            )
        )
    
    # Country
    if "Country" in df.columns:

        path_master = (Path.cwd().parent / "master" / f"country_region.csv")

        df_country_region = (
            spark.read.format("csv")
            .option("header", "true")
            .option("skipRows", 5)
            .load(f"file:{path_master}")
        )

        df = (
            df.join(
                df_country_region,
                on="Country",
                how="left"
            )
            .withColumnRenamed("Region", "Country_Region")
        )
    
    # add missing columns
    for col in include_cols:
        if col not in df.columns:
            df = df.withColumn(col, F.lit(None))

    # type casting
    df = df.select([
        F.col(c).cast(schema_map[c]).alias(c)
        for c in include_cols
    ])

    # add to list
    df_all_years.append(df)

# union all year
df_all = reduce(
    lambda x, y: x.unionByName(y),
    df_all_years
)
    
# save to silver layer
(
    df_all.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable(f"stackoverflow.silver.person")
)