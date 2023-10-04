from pyspark.sql import SparkSession,DataFrame,Row
from pyspark.sql.functions import input_file_name,udf
from pyspark.sql.types import StringType

def get_file_name_from_path(path: str) -> str:
    return path.split("/")[-1].split('.')[0]

get_file_name_from_path_udf = udf(get_file_name_from_path, StringType())

def read_delimited_file(param: dict, spark: SparkSession) -> DataFrame:
    """Read the input source after parsing the config file and storing it in spark data frame

    Args:
        param (dict): dictionary contain all the information about the source file input
        spark (SparkSession): spark session has all configuration that we needed

    Returns:
        DataFrame: return spark data frame that has all the content plus the file name 
    """

    input_cols_names = [field["columnName"] for field in param["inputSchema"]]
    df = spark.read \
        .option("delimiter", param["dataFileDelimiter"]) \
        .option("header", param["header"]) \
        .csv(param["inputSourcePath"]) \
        .withColumn("file_name", get_file_name_from_path_udf(input_file_name()))
    
    return df.toDF(*input_cols_names)


