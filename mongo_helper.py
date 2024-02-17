import pymongo

def get_mongo_client():
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
    return mongo_client

def get_mongo_database(database_name):
    client = get_mongo_client()
    return client[database_name]

def get_mongo_collection(database_name, collection_name):
    databse = get_mongo_database(database_name)
    return databse[collection_name]