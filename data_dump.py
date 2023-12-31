import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")


DATA_FILE_PATH = '/config/workspace/aps_failure_training_set1.csv'

DATABASE_NAME = "aps"

COLLECTion_NAME = "sensor"



if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"No of rows and columns:{df.shape}")

    # convert dataframe into json to dump into mongo db

    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    # inert into mongodb
    client[DATABASE_NAME][COLLECTion_NAME].insert_many(json_record)
