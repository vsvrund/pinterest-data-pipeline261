import requests
from time import sleep
import random
from multiprocessing import Process
import boto3
import json
import sqlalchemy
from sqlalchemy import text
import datetime



random.seed(100)


class AWSDBConnector:

    def __init__(self):

        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306
        
    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine


new_connector = AWSDBConnector()


def run_infinite_post_data_loop():
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            
            for row in pin_selected_row:
                pin_result = dict(row._mapping)

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)


            pin_result = {k: str(v) if isinstance(v, datetime.datetime) else v for k, v in pin_result.items()}
            geo_result = {k: v.strftime("%Y-%m-%d %H:%M:%S") if isinstance(v, datetime.datetime) else v for k, v in geo_result.items()}
            user_result = {k: str(v) if isinstance(v, datetime.datetime) else v for k, v in user_result.items()}



            
            example_df = {"index": 1, "name": "Maya", "age": 25, "role": "engineer"}

            invoke_url = "https://s3r2ivz473.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-0a1e5630c127-pin/record"
            #To send JSON messages you need to follow this structure
            payload = json.dumps({
                "stream-name": "YourStreamName",
                "records":{
                    #Data should be send as pairs of column_name:value, with different columns separated by commas       
                    "value": pin_result
                    },
                    
                
               "PartitionKey": "desired-name"
                })
            headers = {'Content-Type': 'application/json'}
            response = requests.request("PUT", invoke_url, headers=headers, data=payload)


            invoke_url = "https://s3r2ivz473.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-0a1e5630c127-geo/record"
            payload = json.dumps({
                "stream-name": "YourStreamName",
                "records": {
                    #Data should be send as pairs of column_name:value, with different columns separated by commas       
                    "value": geo_result
                    },
                    
                
                "PartitionKey": "desired-name"
                }, default=str)

            headers = {'Content-Type': 'application/json'}
            response = requests.request("PUT", invoke_url, headers=headers, data=payload)

            invoke_url = "https://s3r2ivz473.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-0a1e5630c127-user/record"
            payload = json.dumps({
                "stream-name": "YourStreamName",
                "records":{
                    #Data should be send as pairs of column_name:value, with different columns separated by commas       
                    "value": user_result
                    },
                
                "PartitionKey": "desired-name"
                }, default=str)
            
            headers = {'Content-Type': 'application/json'}
            response = requests.request("PUT", invoke_url, headers=headers, data=payload)
            print(response.json())          
            #print(pin_result)
            #print(geo_result)
            #print(user_result)


if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    
