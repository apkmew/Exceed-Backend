from pymongo import MongoClient
from dotenv import load_dotenv
import os
import urllib
load_dotenv('.env')

user = os.getenv('user')
password = urllib.parse.quote(os.getenv('password'))
client = MongoClient(f'mongodb://{user}:{urllib.parse.quote(password)}@mongo.exceed19.online:8443/?authMechanism=DEFAULT')
db = client['exceed04']