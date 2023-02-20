import extract
from pyspark.sql import SparkSession
from great_expectations.dataset import SparkDFDataset
from datetime import datetime
from uuid import uuid4
import pandas as pd 


spark = SparkSession.builder.master("local[*]").appName("Spotify ETL").getOrCreate()

def data_quality(df):
    raw_test_df = SparkDFDataset(df)
    type(raw_test_df)

    MANDATORY_COLUMNS = [
        "ID",
        "song_names",
        "artist_names",
        "played_at",
        "timestamps"
    ]

    for column in MANDATORY_COLUMNS:
        try: 
            assert raw_test_df.expect_column_to_exist(column).success, f"Mandatory column {column} does not exist: FAILED :("
            print(f"Column {column} existis: PASSED")
        except AssertionError as e:
            print(e)
    
    
    test_result = raw_test_df.expect_column_values_to_be_unique("ID")
    failed_msg = " ".join([f"""oh!""",
        f"""{test_result.result['unexpected_count']} of {test_result.result['element_count']} items""", 
        f"""or {round(test_result.result['unexpected_percent'], 2)}% are not unique: FAILED"""])
    print(f"""{'Column id is unique: PASSED' if test_result.success else failed_msg}""")
    

def transform(data):
    data_raw= []
    for song in data['items']:
        id = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
        data_raw.append({
            "ID": id,
            "song_names": song["track"]["name"],
            "artist_names": song["track"]["album"]["artists"][0]["name"],
            "played_at": song["played_at"],
            "timestamps": song["played_at"][0:10]

        })
    
    df = spark.createDataFrame(data_raw)
    #df.show(100)

    return df 


