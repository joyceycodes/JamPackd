import os
from bson.objectid import ObjectId
import pymongo

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

    def delete_user(self, id: str):
        db = client[dbname]
        plist = db.users.find_one({"_id": ObjectId(id)})
        if plist:
            db.users.delete_one({"_id": ObjectId(id)})

    def update_user(self, id: str, data: dict):
        if len(data) < 1:
            return False
        db = client[dbname]
        user = db.users.find_one({"_id": ObjectId(id)})
        if user:
            updated_user = db.user.update_one(
                {"_id": ObjectId(id)}, {"$set": data}
            )
            if updated_user:
                return True
            return False
