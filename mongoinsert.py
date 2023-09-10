"""For insert csv data"""

import pandas as pd
import csv
import pymongo
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
client_uri = config.get('MyMongoDB', 'client')


myclient = pymongo.MongoClient(client_uri)
db = myclient['MymongoDB']
collection = db[input('date')]



#insert csvfile

csv_file = input("SC_data_date").csv            
with open(csv_file,"r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data_list = [dict(row) for row in reader]


for data in data_list:
    data["_id"] = str(data["id"])
    del data["id"]


insert_result = collection.insert_many(data_list)



if insert_result.acknowledged:
    print("Success")
else:
    print("Insertion failed")

myclient.close()




