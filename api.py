import json
from json import JSONEncoder
from json import dumps
from flask import Flask
import paho.mqtt.client as mqtt
import datetime
from pymongo import MongoClient
from bson import json_util


# Set up client for MongoDB
mongoClient=MongoClient()
db=mongoClient.SensorData
collection=db.home_data
lastOne = collection.find_one()
lastTen = collection.find().sort("_id", -1).limit(10)
all = collection.find().sort("_id", -1).limit(100000)
# ranged = collection.find({"value: { "$gt" :  20, "$lt" : 27}})

#APIs with Flast App
# @Sanket Nalegaonkar
# 14/09/2023
   
app = Flask(__name__)

# Getting Single Recent Records

@app.route("/lastone", methods=['GET'])
    
def getLastOneRecord():
        return json.loads(json_util.dumps(lastOne))

# Getting 10 Recent Records

@app.route("/lastten", methods=['GET'])
    
def getLastTenRecords():
        return json.loads(json_util.dumps(lastTen))

# Getting All Records

@app.route("/all", methods=['GET'])
    
def getAllRecords():
        return json.loads(json_util.dumps(all))

# Getting Range based Records

@app.route("/ranged", methods=['GET'])

def getRangedRecords():
        records = collection.find({"value": { "$gt" :  15, "$lt" : 30}}).sort("_id", -1).limit(1000)
        return json.loads(json_util.dumps(records))

app.run(port=8000)
