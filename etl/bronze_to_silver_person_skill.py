from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField
from functools import reduce
import re
from utils.schema_utils import type_map
from utils.unify_functions import replace_skill_name
from utils.unify_rules import (
    Language_RULES,
    Database_RULES,
    Platform_RULES,
    Webframe_RULES,
    OpSys_RULES
)


years = [2021, 2022, 2023, 2024, 2025]
df_all_years = []

unify_skills = {
    "Language": Language_RULES,
    "Database": Database_RULES,
    "Platform": Platform_RULES,
    "Webframe": Webframe_RULES,
    "OpSys": OpSys_RULES,
}

for year in years:

    # load bronze table
    path_table = f"stackoverflow.bronze.result_{year}"

    df_table = (
        spark.read.table(path_table)
        .replace("NA", None)
    )

    # skill columns
    skill_cols = [
        c for c in df_table.columns
        if (
            c.endswith("HaveWorkedWith")
            or c.endswith("WantToWorkWith")
            or c.startswith("OpSys")
        )
    ]

    df_skill_list = []

    for col_name in skill_cols:

        if col_name.endswith("HaveWorkedWith"):
            category = col_name.removesuffix("HaveWorkedWith")
            experience_type = "Have"

        elif col_name.endswith("WantToWorkWith"):
            category = col_name.removesuffix("WantToWorkWith")
            experience_type = "Want"

        elif col_name == "OpSysPersonal_use":
            category = "OpSys"
            experience_type = "Personal"

        elif col_name in ("OpSysProfessional_use", "OpSys"):
            category = "OpSys"
            experience_type = "Professional"

        # explode skill list
        df_skill = (
            df_table
            .select(
                "ResponseId",
                F.lit(category).alias("Category"),
                F.lit(experience_type).alias("ExperienceType"),
                F.explode(
                    F.split(
                        F.col(col_name),
                        ";"
                    )
                ).alias("Skill"),
                "Year"
            )
            .filter(F.col("Skill").isNotNull())
            .filter(F.trim(F.col("Skill")) != "")
        )

        df_skill_list.append(df_skill)

    # union all skill tables
    df_skill = (
        reduce(
            lambda x, y: x.unionByName(y),
            df_skill_list
        )
        .withColumn(
            "ResponseId",
            F.col("ResponseId").cast("long")
        )
        .withColumn(
            "Skill",
            F.trim("Skill")
        )
        .dropDuplicates()
        .select(
            "ResponseId",
            "Category",
            "ExperienceType",
            "Skill",
            "Year"
        )
    )
    # unify skill names
    df_skill = replace_skill_name(df_skill, unify_skills)

    # add to list
    df_all_years.append(df_skill)

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
    .saveAsTable("stackoverflow.silver.person_skill")
)
