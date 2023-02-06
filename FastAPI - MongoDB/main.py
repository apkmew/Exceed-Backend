from pymongo import MongoClient
from dotenv import load_dotenv
import os
import urllib
load_dotenv('.env')

user = os.getenv('user')
password = urllib.parse.quote(os.getenv('password'))
client = MongoClient(f'mongodb://{user}:{urllib.parse.quote(password)}@mongo.exceed19.online:8443/?authMechanism=DEFAULT')
db = client['exceed04']
collection = db['enrollment_system']

data = [
    {
        'stdID': 360,
        'stdName': 'Mew',
        'Course_name': 'Problem Solving',
        'grade': 4,
        'Unit': 1
    },
    {
        'stdID': 165,
        'stdName': 'Andy',
        'Course_name': 'ADT',
        'grade': 3,
        'Unit': 3
    },
    {
        'stdID': 469,
        'stdName': 'Boss',
        'Course_name': 'Database',
        'grade': 2,
        'Unit': 4
    },
    {
        'stdID': 649,
        'stdName': 'Shoyo',
        'Course_name': 'Sports',
        'grade': 1,
        'Unit': 2
    },
    {
        'stdID': 721,
        'stdName': 'Koro',
        'Course_name': 'Science',
        'grade': 0,
        'Unit': 5
    }
]
#collection.delete_one({'stdID': '360'})
#collection.insert_one({'stdID': '360', 'stdName': 'Mew', 'Course_name': 'CPE', 'grade': 'A+', 'Unit': '3'})
#collection.insert_many(data)
#collection.delete_many({})
#ori_data = collection.find({'stdID': 360})
#if len(list(ori_data)) == 0:
#    print('Not found')
#else:
#    print('Found')
#for i in ori_data:
#    print(i)

#for i in collection.find():
#    print(i)

#collection.delete_one({'Course_name': 'ADT'})

#print('---------------------------------')

#for i in collection.find():
#    print(i)

