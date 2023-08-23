"""Find
fouction of finding collection

"""
import pymongo
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
client_uri = config.get('MyMongoDB', 'client')


try:
    # Try to connect MongoDB
    myclient = pymongo.MongoClient(client_uri)
    # Another way to connect Mongo
    # client = MongoClient(host="localhost", port=27017)
    
    
    database_list = myclient.list_database_names()
    
    if "MyDB" in database_list:
        print("Successfully connected to MongoDB")
    else:
        print("Connected to MongoDB, but 'MyDB' not found.")
except Exception as e:
    print("Error:", e)


# chose DataBase
database_name = "MyDB"
db = myclient[database_name]

# Shows collections
collection_names = db.list_collection_names()
print(f"Available collections in {database_name}:", collection_names)

# chose the specifics collections
collection_name = input("")
collection = db[collection_name]

# search the specifics goods by _id
field_name = "_id"
field_value = input("Enter the _id to finding your goods !: ")


query = {field_name: field_value}
documents = collection.find(query)

for document in documents:
    print(document)




myclient.close()






