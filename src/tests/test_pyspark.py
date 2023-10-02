import pytest
from pyspark.sql.functions import col, regexp_replace
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


@pytest.fixture
def spark_fixture():
    spark = SparkSession.builder.appName("Testing PySpark Example").getOrCreate()
    yield spark

# Create a SparkSession
spark = SparkSession.builder.appName("Testing PySpark Example").getOrCreate()

# Remove additional spaces in name
def remove_extra_spaces(df, column_name):
    # Remove extra spaces from the specified column
    df_transformed = df.withColumn(column_name, regexp_replace(col(column_name), "\\s+", " "))

    return df_transformed

def test_single_space(spark_fixture):
    sample_data = [{"name": "John    D.", "age": 30},
                   {"name": "Alice   G.", "age": 25},
                   {"name": "Bob  T.", "age": 35},
                   {"name": "Eve   A.", "age": 28}]

    # Create a Spark DataFrame
    original_df = spark_fixture.createDataFrame(sample_data)

    expected_data = [{"name": "John    D.", "age": 30},
                     {"name": "Alice   G.", "age": 25},
                     {"name": "Bob  T.", "age": 35},
                     {"name": "Eve   A.", "age": 28}]

    expected_df = spark_fixture.createDataFrame(expected_data)

    diff_df = original_df.subtract(expected_df)

    assert diff_df.count() == 0