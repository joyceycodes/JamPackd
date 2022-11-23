import os
import pymongo
from bson.objectId import ObjectId

dbhost = os.environ["MONGOHOST"]
dbname = os.environ["MONGODATABASE"]
dbuser = os.environ["MONGOUSER"]
dbpass = os.environ["MONGOPASSWORD"]

mongo_str = f"mongodb://{dbuser}:{dbpass}@{dbhost}"

client = pymongo.MongoClient(mongo_str)


class SpotifyQueries:
    def get_recommendations(self):
        pass

    def create_spotify_playlist(self):
        pass

    def update_spotify_playlist(self):
        pass
