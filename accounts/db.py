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
            # change this later to not be a string - Lee
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
        user = db.users.find_one({"_id": ObjectId(id)})
        if user:
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


# Update and Delete are still WIP

# def update_user(self, user_id, data):
#     with pool.connection() as conn:
#         with conn.cursor() as cur:
#             params = [
#                 data.first,
#                 data.last,
#                 data.avatar,
#                 data.email,
#                 data.username,
#                 user_id,
#             ]
#             cur.execute(
#                 """
#                 UPDATE users
#                 SET first = %s
#                 , last = %s
#                 , avatar = %s
#                 , email = %s
#                 , username = %s
#                 WHERE id = %s
#                 RETURNING id, first, last, avatar, email, username
#                 """,
#                 params,
#             )

#             record = None
#             row = cur.fetchone()
#             if row is not None:
#                 record = {}
#                 for i, column in enumerate(cur.description):
#                     record[column.name] = row[i]

#             return record

# def delete_user(self, user_id):
#     with pool.connection() as conn:
#         with conn.cursor() as cur:
#             cur.execute(
#                 """
#                 DELETE FROM users
#                 WHERE id = %s
#                 """,
#                 [user_id],
#             )
