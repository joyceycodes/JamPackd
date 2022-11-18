import os
from psycopg_pool import ConnectionPool
import pymongo
import bson

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])

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

    def get_playlist(self, id):
        db = client[dbname]
        result = db.users.findone({"_id": id})
        if result:
            result["id"] = result["_id"]
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
