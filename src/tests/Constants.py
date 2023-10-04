from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql import Row

expected_json_parsed = {
  "sourceName": "3G_ERCSN",
  "rejection": {
    "rejectedRecordsPath": "/home/moustafa/Scala/spark-etl-demo/data/processed/3G_ERCSN/",
    "rejectOutputType": "csv"
  },
  "inputSource": {
    "inputFilesType":"csv",
    "dataFileDelimiter": "|",
    "totalInputFileColumns": "5",
    "inputSourcePath": "C:/Users/Mahmoud Alaa/Desktop/ETL_Project/Python_ETL/data/raw_zone/3G_ERCSN/ercsn_4g_20200512182929_part02_processing.csv",
    "processingSuffix": "*_processing",
    "header": "false",
    "inputSchema": [
      {
        "columnName": "imsi",
        "columnType": "StringType",
        "isNullable": False
      },
      {
        "columnName": "imei",
        "columnType": "StringType",
        "isNullable": True
      },
      {
        "columnName": "cell",
        "columnType": "IntegerType",
        "isNullable": False
      },
      {
        "columnName": "lac",
        "columnType": "IntegerType",
        "isNullable": False
      },
      {
        "columnName": "eventType",
        "columnType": "StringType",
        "isNullable": True
      },
      {
        "columnName": "eventTs",
        "columnType": "TimestampType",
        "isNullable": False
      },
      {
        "columnName": "file_name",
        "columnType": "StringType",
        "isNullable": False
      }
    ]
  },
  "targetSource": [
    {
      "targetTable": "Singl_KPI",
      "targetSchema": "mod",
      "partitionColumns": "event_date,batch_id",
      "outputFormat": "orc",
      "saveMode": "Append"
    }
  ]

}



ETL_INPUT_FILE_NAME_TEST = "ercsn_4g_20200512182929_part02_processing"

ercsn_schema_type = StructType([
    StructField("imsi", StringType(), True),
    StructField("imei", StringType(), True),
    StructField("cell", StringType(), True),
    StructField("lac", StringType(), True),
    StructField("eventType", StringType(), True),
    StructField("eventTs", StringType(), True),
    StructField("file_name", StringType(), True)
])


expected_valid_seq = [
      Row(
        "310120265624299",
        "490154203237518",
        "1234",
        "99",
        "1",
        "2020-06-15 07:45:43",
        ETL_INPUT_FILE_NAME_TEST
      ),
      Row(
        "310120265624299",
        "490154203237518",
        "5432",
        "54",
        "2",
        "2020-06-15 12:12:43",
        ETL_INPUT_FILE_NAME_TEST
      ),
      Row(
        "310120265624299",
        "490154203237518",
        "4321",
        "54",
        "1",
        "2020-06-15 15:41:43",
        ETL_INPUT_FILE_NAME_TEST
      ),
      Row(
        "310120265624299",
        "490154203237518",
        "4657",
        "99",
        "4",
        "2020-06-15 19:11:43",
        ETL_INPUT_FILE_NAME_TEST
      ),
      Row(
        "310120265624299",
        "490154203237518",
        "1234",
        "99",
        "3",
        "2020-06-15 20:00:43",
        ETL_INPUT_FILE_NAME_TEST
      ),
      Row(
        "310120265624234",
        "490154203237543",
        "123",
        "22",
        "1",
        "2020-06-15 12:12:43",
        ETL_INPUT_FILE_NAME_TEST
      ),
      Row(
        "310120265624234",
        "490154203237543",
        "456",
        "21",
        "1",
        "2020-06-15 15:31:43",
        ETL_INPUT_FILE_NAME_TEST
      ),
      Row(
        "310120265624234",
        "490154203237543",
        "567",
        "65",
        "2",
        "2020-06-15 17:53:43",
        ETL_INPUT_FILE_NAME_TEST
      ),
      Row(
        "310120265624234",
        "490154203237543",
        "543",
        "66",
        "2",
        "2020-06-15 20:13:43",
        ETL_INPUT_FILE_NAME_TEST
      ),
      Row(
        "310120265624234",
        "490154203237543",
        "4978",
        "33",
        "4",
        "2020-06-15 22:12:43",
        ETL_INPUT_FILE_NAME_TEST
      ),
      Row(
        "310120265624654",
        "490154203237654",
        "4367",
        "22",
        "1",
        "2020-06-15 12:12:43",
        ETL_INPUT_FILE_NAME_TEST
      ),
      Row(
        "310120265624123",
        "490154203231245",
        "2435",
        "11",
        "1",
        "2020-06-15 12:12:43",
        ETL_INPUT_FILE_NAME_TEST
      ),
      Row(
        "310120265627654",
        "490154203235432",
        "1235",
        "43",
        "1",
        "2020-06-15 12:12:43",
        ETL_INPUT_FILE_NAME_TEST
      ),
      Row(
        None,
        "3214324134",
        "21421",
        "12421",
        "2",
        "2020-06-15 12:12:43",
        ETL_INPUT_FILE_NAME_TEST
      ),
      Row(
        "214214",
        "12421412421124",
        None,
        "124",
        "1",
        "2020-06-15 12:12:43",
        ETL_INPUT_FILE_NAME_TEST
      ),
      Row(
        "214214",
        "12421412421124",
        "11",
        None,
        "1",
        "2020-06-15 12:12:43",
        ETL_INPUT_FILE_NAME_TEST
      ),
      Row(
        "214214",
        "12421412421124",
        "11",
        "444",
        "1",
        None,
        ETL_INPUT_FILE_NAME_TEST
      )
]