#load file
from config import USER, PW, DB_NAME, HOST_NAME
import extract
import transform
import mysql.connector
from mysql.connector import Error
import pandas as pd
import sqlalchemy
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Extract and transform
    data = extract.extract_data()    
    data_ordered = transform.transform(data)
    validated_df = transform.data_quality(data_ordered)
    
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
            cursor.execute("CREATE DATABASE {0}".format(DB_NAME))
            cursor.execute("USE {0}".format(DB_NAME))
            print("database is created")  
            
            try:
                #create the table and save the data
                df.to_sql("my_played_tracks", engine)
                print("The table has been created and the data has been successfully!!")
            except:
                print("This table already exists")
            connection.close()
    except Error as err:
        print(f"Error: '{err}'")
    
 
   
    


