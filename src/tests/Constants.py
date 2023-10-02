expected_json_parsed = {
        'sourceName': '3G_ERCSN',
        'inputSource': {
                'inputFilesType': 'csv',
                'dataFileDelimiter': '|',
                'totalInputFileColumns': '5',
                'inputSourcePath': '/home/moustafa/Scala/spark-etl-demo/data/raw_zone/3G_ERCSN/',
                'processingSuffix': '*_processing',
                'header': 'false',

                'inputSchema': [
                    {'columnName': 'imsi', 'columnType': 'StringType', 'isNullable': False},
                    {'columnName': 'imei', 'columnType': 'StringType', 'isNullable': True},
                    {'columnName': 'cell', 'columnType': 'IntegerType', 'isNullable': False},
                    {'columnName': 'lac', 'columnType': 'IntegerType', 'isNullable': False},
                    {'columnName': 'eventType', 'columnType': 'StringType', 'isNullable': True},
                    {'columnName': 'eventTs', 'columnType': 'TimestampType', 'isNullable': False},
                    {'columnName': 'fileName', 'columnType': 'StringType', 'isNullable': False}
                ]
        },
        'rejection': {
                'rejectedRecordsPath': '/home/moustafa/Scala/spark-etl-demo/data/processed/3G_ERCSN/',
                'rejectOutputType':  "csv"
        },
        "targetSource": [
            {
                "targetTable":  "Singl_KPI",
                "targetSchema":  "mod",
                "partitionColumns":  "event_date,batch_id",
                "outputFormat":  "orc",
                "saveMode":  "Append"
            }
        ]
    }