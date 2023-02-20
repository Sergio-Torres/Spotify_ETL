from config import USER, PW, DB_NAME, HOST_NAME
import extract
import transform
import mysql.connector
from mysql.connector import Error
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql import Row
import sqlalchemy
from sqlalchemy.orm import sessionmaker

#spark = SparkSession.builder.appName('SparkByExamples.com').config("spark.jars", "mysql-connector-j_8.0.32-1ubuntu22.10_all.deb").getOrCreate()

if __name__ == "__main__":
    # Extract and transform
    data = extract.extract_data()    
    data_ordered = transform.transform(data)
    validated_df = transform.data_quality(data_ordered)
    #data_rdd = data_ordered.rdd
    df = data_ordered.toPandas()
    
    engine = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.format(USER, PW,HOST_NAME,DB_NAME))
    #DB connection
    try:
        connection = mysql.connector.connect(
            host = HOST_NAME,
            user = USER,
            password = PW
            )

        if connection.is_connected():
            cursor = connection.cursor()
            #cursor.execute("CREATE DATABASE {0}".format(DB_NAME))
            cursor.execute("USE {0}".format(DB_NAME))
            print("database is created")

            query = """
                CREATE TABLE IF NOT EXISTS my_played_tracks(
                ID INT PRIMARY KEY,
                song_name VARCHAR(200),
                artist_name VARCHAR(200),
                played_at VARCHAR(200),
                timestamp VARCHAR(200)
               )
            """
        
            cursor.execute(query)
            print("The table has been created successfully!!")
            
            df.to_sql("los_played_tracks", engine)
            connection.close()
    except Error as err:
        print(f"Error: '{err}'")
    
 
   
    
""""    engine = ce('mysql+pymysql://{0}:{1}@{2}/{3}'.format(USER, PW,HOST_NAME,DB_NAME))
    conn = mysql.connector.connect(engine)
    cursor = conn.cursor()
    
    query = ""
       ""
    cursor.execute(query)
    print("la conexion a la db funciona")

    try:
        data.to_sql("played_tracks", engine, index=False, if_exists='append')
    except:
        print("Data already exists in the database")
#    engine.execute('CREATE DATABASE {0}'.format(DB_NAME))

    

    conn.close() 
    print("close db successfully")"""
