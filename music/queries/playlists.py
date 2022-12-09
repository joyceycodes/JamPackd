import os
from bson.objectid import ObjectId
import pymongo


# dbhost = os.environ["MONGOHOST"]
dbname = os.environ["MONGODATABASE"]
# dbuser = os.environ["MONGOUSER"]
# dbpass = os.environ["MONGOPASSWORD"]


# mongo_str = f"mongodb://{dbuser}:{dbpass}@{dbhost}"
mongo_str = os.environ["DATABASE_URL"]

client = pymongo.MongoClient(mongo_str)


class PlaylistQueries:
    def get_all_playlists(self, user_id):
        db = client[dbname]
        result = list(db.playlists.find({"user_id": user_id}))
        return result

    def get_playlist(self, playlist_id, user_id):
        print("***get", user_id)

        db = client[dbname]
        result = db.playlists.find_one({"_id": ObjectId(playlist_id)})

        if result:
            result["id"] = str(result["_id"])
            if result["user_id"] != user_id:
                return None
        return result

    def create_playlist(self, data, user_id):
        print(user_id)
        db = client[dbname]
        props = data.dict()
        props["user_id"] = user_id
        result = db.playlists.insert_one(props)
        # print("INSERTED ID:", result.inserted_id)
        if result.inserted_id:
            result = self.get_playlist(str(result.inserted_id), user_id)
            result["id"] = str(result["_id"])
            # print(result["id"], str(result["_id"]))
            return result

    def update_playlist(self, _id: str, data):
        db = client[dbname]
        result = db.playlists.find_one({"_id": ObjectId(_id)})
        user_id = result["user_id"]
        if result:
            result = db.playlists.update_one(
                {"_id": ObjectId(_id)}, {"$set": data.dict()}
            )
            result = self.get_playlist(_id, user_id)
            result["id"] = str(result["_id"])
            return result

    def delete_playlist(self, id: str):
        db = client[dbname]
        plist = db.playlists.find_one({"_id": ObjectId(id)})
        if plist:
            db.playlists.delete_one({"_id": ObjectId(id)})
