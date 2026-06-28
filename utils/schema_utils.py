from pyspark.sql.types import *

type_map = {
    "string": StringType(),
    "integer": IntegerType(),
    "int": IntegerType(),
    "long": LongType(),
    "double": DoubleType(),
    "float": FloatType(),
    "boolean": BooleanType(),
    "date": DateType(),
    "timestamp": TimestampType(),
}
