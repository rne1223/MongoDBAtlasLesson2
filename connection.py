from pymongo import MongoClient
from dotenv import load_dotenv
import os

MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)

for db_name in client.list_database_names():
    print(db_name)


client.close()