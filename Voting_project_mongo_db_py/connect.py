import pymongo
import random


connection = pymongo.MongoClient("", 27017)  # to add mongo_db link
database = connection["new_db"]
collection = database["user_info"]


if __name__ == '__main__':

    while True:
        user_id = random.randint(10, 10000)
        try:

            user_email: str = input("Enter your email:")
            user_password: str = input("Enter your password:")
            user_phone: int = int(input("Enter your phone number:"))

            data = {"_id": user_id, "Email": user_email, "Password": user_password, "Phone": user_phone}
            ids = collection.insert_one(data)
            print("ids", ids.inserted_id)

        except Exception as err:
            print(err)
