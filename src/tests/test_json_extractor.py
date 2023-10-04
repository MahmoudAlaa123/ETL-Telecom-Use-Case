from json_extractor import JsonExtractor 

def test_extract_json_from_str() -> dict:
    simple_json_str = """{"name":"Moustafa","age":3}"""
    expected_json_obj = {"name":"Moustafa","age":3}
    actual_json_obj = JsonExtractor.extract_json_from_str(simple_json_str)
    assert expected_json_obj == actual_json_obj



def test_get_json_parsed_from_file() -> dict:
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
    
    actual_json_parsed = JsonExtractor.get_json_parsed_from_file("config.json")

    assert actual_json_parsed == expected_json_parsed
    



    