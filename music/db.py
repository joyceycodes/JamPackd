import os
import pymongo
from bson.objectid import ObjectId


dbhost = os.environ["MONGOHOST"]
dbname = os.environ["MONGODATABASE"]
dbuser = os.environ["MONGOUSER"]
dbpass = os.environ["MONGOPASSWORD"]


mongo_str = f"mongodb://{dbuser}:{dbpass}@{dbhost}"

client = pymongo.MongoClient(mongo_str)


class PlaylistQueries:
    def get_all_playlists(self):
        db = client[dbname]
        result = list(db.music.find())
        for value in result:
            value["id"] = value["_id"]
        return result

    def get_playlist(self, id):
        db = client[dbname]
        result = db.music.find_one({"_id": ObjectId(id)})
        if result:
            result["id"] = str(result["_id"])
        return result

    def create_playlist(self, data):
        db = client[dbname]
        result = db.music.insert_one(data.dict())
        if result.inserted_id:
            result = self.get_playlist(str(result.inserted_id))
            result["id"] = str(result["_id"])
            return result

    def update_playlist(self, _id: str):
        db = client[dbname]
        result = db.music.find_one({"_id": ObjectId(_id)})
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", result)
        if result.id:
            result = self.update_playlist({"_id": ObjectId(_id)})
            result["id"] = str(result["_id"])
            return result

    def delete_playlist(self, id: str):
        db = client[dbname]
        plist = db.music.find_one({"_id": ObjectId(id)})
        if plist:
            db.music.delete_one({"_id": ObjectId(id)})
