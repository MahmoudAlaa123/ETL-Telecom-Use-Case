from pyspark.sql import SparkSession
from tests.Constants import expected_valid_seq, ercsn_schema_type
from common.hadoop_file_handler import read_delimited_file
from json_extractor import JsonExtractor
import pytest
from pyspark import SparkConf, SparkContext

@pytest.fixture(scope="session")
def spark_fixture():
    # Initialize Spark
    conf = SparkConf().setAppName("MyApp")
    sc = SparkContext(conf=conf)

    # Add your Python file
    sc.addPyFile("C:/Users/Mahmoud Alaa/Desktop/ETL_Project/Python_ETL/src/common.zip")

    # Initialize SparkSession
    spark = SparkSession.builder.appName("Testing PySpark DataFrame").getOrCreate()

    yield spark  # provide the fixture value

    spark.stop()  # cleanup after the test is over


param = JsonExtractor.get_json_parsed_from_file("config.json")

def test_read_delimited_file(spark_fixture) -> bool:
        
        

    expected_df = spark_fixture.createDataFrame(expected_valid_seq, ercsn_schema_type)
    actual_df = read_delimited_file(param["inputSource"],spark=spark_fixture)
    diff = expected_df.subtract(actual_df)
    assert expected_df.collect() == actual_df.collect()


