import server
from database_model import Auction_DB_Model
import random


class Observer:
    # def __init__(self):
    #     self.observer_data = server.Auction_Server()

    def receive_data(self, data):

        print(data)
        return data

    def send_data(self, data):
        return data


class Admin:

    def __int__(self):
        pass

    def insert_data(self):
        database: Auction_DB_Model = Auction_DB_Model()
        collection = database.product()

        item_name = input("Enter the name of the item:")
        item_name = item_name.replace(' ', '_')
        reserve_price = int(input("Enter the reserve price for the item:"))
        code = ""

        for i in range(2):
            x = random.randint(65, 90)
            code += chr(x)
        for i in range(2):
            x = random.randint(48, 57)
            code += chr(x)

        data_form = {"Item Name": item_name, "Reserve Price": reserve_price, "Code": code}

        collection.insert_one(data_form)


# if __name__ == "__main__":
#     admin = Admin()
#     admin.insert_data()
