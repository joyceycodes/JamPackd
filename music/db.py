import os
import pymongo
from bson.objectid import ObjectId

# pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])

dbhost = os.environ["MONGOHOST"]
dbname = os.environ["MONGODATABASE"]
dbuser = os.environ["MONGOUSER"]
dbpass = os.environ["MONGOPASSWORD"]


mongo_str = f"mongodb://{dbuser}:{dbpass}@{dbhost}"

client = pymongo.MongoClient(mongo_str)


class PlaylistQueries:
    def get_all_playlists(self):
        db = client[dbname]
        result = list(db.users.find())
        for value in result:
            value["id"] = value["_id"]
        return result

    def get_playlsit(self, id):
        db = client[dbname]
        result = db.users.find_one({"_id": ObjectId(id)})
        if result:
            result["id"] = str(result["_id"])
        return result

    def create_playlist(self, data):
        db = client[dbname]
        result = db.users.insert_one(data.dict())
        if result.inserted_id:
            result = self.get_user(result.inserted_id)
            result["id"] = str(result["id"])
            return result

    def update_playlist(self, pl_id, data):
        pass

    def delete_playlist(self, pl_id):
        pass


class SongQueries:
    def get_all_songs(self):
        db = client[dbname]
        result = list(db.songs.find())
        for value in result:
            value["id"] = value["_id"]
        return result

    def get_song(self, id):
        db = client[dbname]
        result = db.songs.find_one({"_id": ObjectId(id)})
        if result:
            result["id"] = str(result["_id"])
        return result

    def create_song(self, data):
        db = client[dbname]
        result = db.songs.insert_one(data.dict())
        print("result 1: *******************", result)
        if result.inserted_id:
            result = self.get_song(str(result.inserted_id))
            print("*****************result", result)
            result["id"] = str(result["id"])
            # result["id"] = str(result["id"])
            return result

    def update_song(self, _id, data):
        pass

    def delete_song(self, _id):
        pass
