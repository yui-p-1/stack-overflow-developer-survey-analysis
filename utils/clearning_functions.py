from pyspark.sql import functions as F

# contains
def build_contains_expr(
    col_name: str,
    rules,
    default_value: str = "Other",
    null_value: str = "Unknown"
):
    expr = None

    for pattern, label in rules:
        condition = F.lower(F.col(col_name)).contains(pattern.lower())

        if expr is None:
            expr = F.when(condition, label)
        else:
            expr = expr.when(condition, label)

    return (
        F.when(F.col(col_name).isNull(), null_value)
         .otherwise(expr.otherwise(default_value))
    )

# exact
def build_exact_expr(
    col_name: str,
    rules,
    default_value: str = "Other",
    null_value: str = "Unknown"
):
    expr = None

    for pattern, label in rules:
        condition = F.col(col_name) == pattern

        if expr is None:
            expr = F.when(condition, label)
        else:
            expr = expr.when(condition, label)

    return (
        F.when(F.col(col_name).isNull(), null_value)
         .otherwise(expr.otherwise(default_value))
    )

# startswith
def build_startswith_expr(
    col_name: str,
    rules,
    default_value: str = "Other",
    null_value: str = "Unknown"
):
    expr = None

    for pattern, label in rules:
        condition = F.col(col_name).startswith(pattern)

        if expr is None:
            expr = F.when(condition, label)
        else:
            expr = expr.when(condition, label)

    return (
        F.when(F.col(col_name).isNull(), null_value)
         .otherwise(expr.otherwise(default_value))
    )

# special
# YearsCode
def build_yearscode_expr(col_name):
    return (
        F.when(F.col(col_name) == "Less than 1 year", F.lit(0))
         .when(F.col(col_name) == "More than 50 years", F.lit(50))
         .otherwise(F.expr(f"try_cast({col_name} as int)"))
    )