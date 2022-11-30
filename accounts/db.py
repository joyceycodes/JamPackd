import os
import pymongo
from bson.objectid import ObjectId

from pydantic import BaseModel

dbhost = os.environ["MONGOHOST"]
dbname = os.environ["MONGODATABASE"]
dbuser = os.environ["MONGOUSER"]
dbpass = os.environ["MONGOPASSWORD"]

mongo_str = f"mongodb://{dbuser}:{dbpass}@{dbhost}"

client = pymongo.MongoClient(mongo_str)


class UserIn(BaseModel):
    full_name: str
    email: str
    password: str


class UserOut(BaseModel):
    id: int | str
    full_name: str
    email: str


class UsersOut(BaseModel):
    users: list[UserOut]


class UserOutWithPassword(BaseModel):
    hashed_password: str
    id: int | str
    full_name: str
    email: str


class DuplicateAccountError(ValueError):
    pass


class UserQueries:
    def get_all_users(self):
        db = client[dbname]
        result = list(db.users.find())
        for value in result:
            value["id"] = value["_id"]
        return result

    def get_user(self, email: str):
        db = client[dbname]
        result = db.users.find_one({"email": email})
        if result:
            # change this later to not be a string - Lee
            result["id"] = str(result["_id"])
        return UserOutWithPassword(**result)

    def create_user(
        self, account: UserIn, hashed_password: str
    ) -> UserOutWithPassword:
        db = client[dbname]
        props = account.dict()
        props["hashed_password"] = hashed_password
        props.pop("password")
        try:
            db.users.insert_one(props)
        except DuplicateAccountError:
            raise DuplicateAccountError()
        props["id"] = str(props["_id"])
        return UserOutWithPassword(**props)

        # result = db.users.insert_one(data.dict())
        # if result.inserted_id:
        #     result = self.get_user(str(result.inserted_id))
        #     result["id"] = str(result["_id"])
        #     return result

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
