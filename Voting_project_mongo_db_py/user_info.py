import pymongo
import random


connection = pymongo.MongoClient("mongodb+srv://ZiDunn:DgKSyyMopDlVQQBl@cluster0.diludbd.mongodb.net/", 27017)
database = connection["new_db"]
collection = database["user_info"]


for i in range(10):
    user_id = random.randint(10, 10000)
    user_email = "zidunn" + str(i) + "@gmail.com"
    user_password = "4546123"
    user_phone: int = 456889
    point: int = 100

    info = "User data is zidunn" + str(i) + " id: " + str(user_id)

    data = {"_id": user_id, "Email": user_email, "Password": user_password, "Phone": user_phone, "Info": info, "Point": point}
    ids = collection.insert_one(data)


