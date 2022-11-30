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


# class DuplicateAccountError(ValueError):
#     pass


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
            result["id"] = str(result["_id"])
        return UserOutWithPassword(**result)

    def create_user(
        self, account: UserIn, hashed_password: str
    ) -> UserOutWithPassword:
        db = client[dbname]
        props = account.dict()
        props["hashed_password"] = hashed_password
        props.pop("password")
        print("AAAAAAAAAA PROPS AAAAAAAAAAAAAAAAAAAAA!!!!!!", props)
        # try:
        db.users.insert_one(props)
        # except DuplicateAccountError:
        #     raise DuplicateAccountError()

        # got rid of this exception for testing

        props["id"] = str(props["_id"])
        return UserOutWithPassword(**props)

    def delete_user(self, id: str):
        db = client[dbname]
        user = db.users.find_one({"_id": ObjectId(id)})
        if user:
            db.users.delete_one({"_id": ObjectId(id)})
