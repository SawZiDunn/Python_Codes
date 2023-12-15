import pymongo
import random


connection = pymongo.MongoClient("###", 27017) # mongo db link
database = connection["new_db"]
collection = database["candidate_info"]


for i in range(10):
    user_id = random.randint(10, 10000)
    candidate_name = "john" + str(i)
    user_phone: int = 456889
    point: int = 100

    info = "User data is John" + str(i) + " id: " + str(user_id)

    data = {"_id": user_id, "Name": candidate_name,"Phone": user_phone, "Info": info, "Point": point}
    ids = collection.insert_one(data)


