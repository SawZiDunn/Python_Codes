import pymongo


class Auction_DB_Model:
    def __init__(self):
        pass

    def connect(self, col_name):
        connection = pymongo.MongoClient("mongodb+srv://ZiDunn:DgKSyyMopDlVQQBl@cluster0.diludbd.mongodb.net/", 27017)
        database = connection["new_db"]
        collection = database[col_name]
        return collection

    def product(self):
        collection = self.connect("product_info")

        return collection

    def candidate(self):
        collection = self.connect("candidate")
        return collection

    def user_info(self):
        collection = self.connect("user_info")
        return collection

    def info(self):
        collection = self.connect("user_info")
        return collection
