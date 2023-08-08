import pymongo

connection = pymongo.MongoClient("mongodb+srv://ZiDunn:DgKSyyMopDlVQQBl@cluster0.diludbd.mongodb.net/", 27017)
database = connection["new_db"]
collection = database["user_info"]
register_email = input("Enter your email to register:")

for i in collection.find({}, {"_id": 0, "Email": 1}):
    if register_email == i["Email"]:
        print("This email is already registered.")
        break
