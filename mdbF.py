import pymongo
from pymongo import MongoClient
from bson import ObjectId
from decouple import config

#mainDB (AWS)
m_DB_link = config("DB")
m_DB_name = config("DB_NAME")
m_DB_collection = config("DB_COLLECTION")

cluster = MongoClient(m_DB_link)
db = cluster[m_DB_name]
collection = db[m_DB_collection]
prefixObject = config("prefixObjectID")
logsChannelObject = config("logsObjectID")
tempRoleHolder = config("tempRoleHolder")


def setOID(type: str):
    if(type == None):
        return None
    if(type == "prefix"):
        obj = ObjectId(f"{prefixObject}")
        return obj
    elif(type == "logschannel"):
        obj = ObjectId(f"{logsChannelObject}")
        return obj
    elif(type == "temproleholder"):
        obj = ObjectId(f"{tempRoleHolder}")
        return obj


def remove_data(key, t: str):
    db_obj = setOID(t)
    removed = collection.update_one(
        {"_id": db_obj},
        {
            "$unset": {
                key: ""
            }
        }
    )


def insert_data(key, value, t: str):
    db_obj = setOID(t)
    # used to insert only one data in used objID
    insertOne = collection.update_one(
        {"_id": db_obj},
        {
            "$set": {
                key: value
            }
        }
    )
    print("[NEW DATA] Single Data Inserted")


def insert_bulk_data(_data, t: str):
    # used to insert bulk data (like multiple item)
    # creates each new ID per {...} data
    # For Example:
    # data = [
    # {item:"1",price:12},
    # {item:"2",price:52},
    # {item:"3",price:32}
    # ]

    collection.insert_many(_data)
    print("[NEW DATA] Bulk Data Inserted")

# def sort_data(key,sortT):
# 	collection.aggregate(
# 	[
# 		{ "$sort" : { key : sortT } }
# 	]
# 	)


def load_data(t: str):
    db_obj = setOID(t)
    data = collection.find_one({"_id": db_obj})
    # all_data = list(data)
    return data


def save_data(key, value, t: str):
    db_obj = setOID(t)
    update = collection.update_one(
        {"_id": db_obj},
        {
            "$set": {
                key: value
            }
        }
    )


def save_to_array(key, value, t: str):
    db_obj = setOID(t)
    update = collection.update_one(
        {"_id": db_obj},
        {
            "$push": {
                key: value
            }
        }
    )


def remove_from_array(key, value, t: str):
    db_obj = setOID(t)
    update = collection.update_one(
        {"_id": db_obj},
        {
            "$pull": {
                key: value
            }
        }
    )
