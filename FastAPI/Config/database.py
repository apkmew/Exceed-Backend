from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv('.env')

user = os.getenv('user')
password = os.getenv('password')
client = MongoClient(f'mongodb://{user}:{password}@mongo.exceed19.online:8443/?authMechanism=DEFAULT')
db = client['exceed04']