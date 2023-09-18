import redis
import json
from bson.json_util import dumps
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
redisClient = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

database = client['SensorData'] #database name in mongodb
recordList = database['home_data'].find() #collection name in 'DummyDb' database

serializedObj = dumps(recordList) #serialize object for the set redis.
print(serializedObj)
result = redisClient.set('records', serializedObj) #set serialized object to redis server.

#you can check the users in redis using redis gui or type 'get users' to redis client or just get it from the redis like below.
parsedRecordList = json.loads(redisClient.get('records'))

for record in parsedRecordList: #check the names
	print(record["_id"]) #'username' one of the field of the 'Users' collection  