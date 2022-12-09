import os
from bson.objectid import ObjectId
import pymongo


dbhost = os.environ["MONGOHOST"]
dbname = os.environ["MONGODATABASE"]
dbuser = os.environ["MONGOUSER"]
dbpass = os.environ["MONGOPASSWORD"]


mongo_str = f"mongodb://{dbuser}:{dbpass}@{dbhost}"


client = pymongo.MongoClient(mongo_str)


class PlaylistQueries:
    # def get_all_playlists(self):
    # db = client[dbname]
    # result = list(db.playlists.find())
    # return result

    def get_all_playlists(self, user_id):
        db = client[dbname]
        result = list(db.playlists.find({"user_id": user_id}))
        return result

    # def get_playlist(self, playlist_id):
    #     db = client[dbname]
    #     result = db.playlists.find_one({"_id": ObjectId(playlist_id)})
    #     if result:
    #         result["id"] = str(result["_id"])
    #     return result

    def get_playlist(self, playlist_id, user_id):
        db = client[dbname]
        result = db.playlists.find_one({"_id": ObjectId(playlist_id)})
        if result:
            result["id"] = str(result["_id"])
            if result["user_id"] != user_id:
                return None
        return result

    def create_playlist(self, data, user_id):
        db = client[dbname]
        result = db.playlists.insert_one(data.dict())
        # print("INSERTED ID:", result.inserted_id)
        if result.inserted_id:
            result = self.get_playlist(
                str(result.inserted_id),
            )
            result["id"] = str(result["_id"])
            print(result["id"], str(result["_id"]))
            return result

    def update_playlist(self, _id: str, data):
        db = client[dbname]
        result = db.playlists.find_one({"_id": ObjectId(_id)})
        if result:
            result = db.playlists.update_one(
                {"_id": ObjectId(_id)}, {"$set": data.dict()}
            )
            result = self.get_playlist(_id)
            result["id"] = str(result["_id"])
            return result

    def delete_playlist(self, id: str):
        db = client[dbname]
        plist = db.playlists.find_one({"_id": ObjectId(id)})
        if plist:
            db.playlists.delete_one({"_id": ObjectId(id)})
