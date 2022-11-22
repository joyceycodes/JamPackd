import os
import pymongo
from bson.objectid import ObjectId

dbhost = os.environ["MONGOHOST"]
dbname = os.environ["MONGODATABASE"]
dbuser = os.environ["MONGOUSER"]
dbpass = os.environ["MONGOPASSWORD"]

mongo_str = f"mongodb://{dbuser}:{dbpass}@{dbhost}"

client = pymongo.MongoClient(mongo_str)


class UserQueries:
    def get_all_users(self):
        db = client[dbname]
        result = list(db.users.find())
        for value in result:
            value["id"] = value["_id"]
        return result

    def get_user(self, id):
        db = client[dbname]
        result = db.users.find_one({"_id": ObjectId(id)})
        if result:
            result["id"] = str(result["_id"])
        return result

    def create_user(self, data):
        db = client[dbname]
        result = db.users.insert_one(data.dict())
        if result.inserted_id:
            result = self.get_user(str(result.inserted_id))
            result["id"] = str(result["_id"])
            return result
