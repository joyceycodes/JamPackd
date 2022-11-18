import os
from psycopg_pool import ConnectionPool

dbhost = os.environ["MONGOHOST"]
dbname = os.environ["MONGODATABASE"]
dbuser = os.environ["MONGOUSER"]
dbpass = os.environ["MONGOPASSWORD"]

mongo_str = f"mongodb://{dbuser}:{dbpass}@{dbhost}"

client = pymongo.MongoClient(mongo_str)

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])


class GetPlaylists:
    def get_all_playlists(self):
        pass
