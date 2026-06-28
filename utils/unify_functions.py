from pyspark.sql import functions as F

# exact
def replace_skill_name(df, unify_skills):
    expr = F.col("Skill")

    for category, rules in unify_skills.items():
        for before, after in rules:
            expr = F.when(
                (F.col("Category") == category) &
                (F.col("Skill") == before),
                after
            ).otherwise(expr)

    return df.withColumn("Skill", expr)