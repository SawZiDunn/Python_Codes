import socket
import server_encrypt_decrypt
import observer
from database_model import Auction_DB_Model
import json


class Auction_Server:

    def __init__(self):
        self.server_ip = "localhost"
        self.server_port = 9998

        self.observer = observer.Observer()

        self.request_control: Request_Control = Request_Control()

        self.decrypted_actual_data = []

    def main(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.server_ip, self.server_port))
        server.listen()

        print("Server is listening on IP: {} and Port: {}.".format(self.server_ip, self.server_port))

        try:
            while True:
                client, address = server.accept()
                print("Connection accepted from {}.".format(address))
                self.client_control(client)

        except Exception as err:
            print(err)

    def client_control(self, client_socket):
        encryption = server_encrypt_decrypt.A3_Encryption()
        decryption = server_encrypt_decrypt.A3_Decryption()

        with client_socket as sock:

            received_data = sock.recv(1024).decode('utf-8')
            actual_data: str = decryption.start_decryption(received_data)

            print("This is actual data:", actual_data)

            actual_data_list = actual_data.split(' ')

            if actual_data_list[0] == "info":
                data = self.request_control.getting_data_info(actual_data_list)
                # print("data ready from server before sending")
                # print(data, type(data))

            elif actual_data_list[0] == "login":
                print("this is log in working")
                data: str = self.request_control.login(actual_data_list)

                ob_send = self.observer.send_data(data)
                print("Ob send:", ob_send)

            elif actual_data_list[0] == "auction":
                print("this is auction working")
                data: str = self.request_control.auction_check(actual_data_list)

            elif actual_data_list[0] == "register":
                data: str = self.request_control.register(actual_data_list)

            else:
                print("Not Info")

            self.observer.receive_data(actual_data)

            encrypted_data: str = encryption.start_encryption(data, "key")
            sock.send(bytes(encrypted_data, 'utf-8'))
            # print("already sent")

    def for_observer(self):
        to_return = self.decrypted_actual_data
        self.decrypted_actual_data = None
        return to_return


class Request_Control:
    def __init__(self):
        self.database = Auction_DB_Model()

    # def info(self, data_list):
    #
    #     collection = self.database.info()
    #     print("collection received")
    #     doc = ""
    #     for i in collection.find({}, {"_id": 0}):
    #         doc += i['info']
    #     print(doc, type(doc), "from request control class")
    #     return doc

    def getting_data_info(self, data_list):
        data: dict = {}
        collection = self.database.info()

        for i in collection.find({}, {"_id": 0}):
            ids = len(data)
            data_form = {"email": i["Email"], "password": i["Password"], "phone": i["Phone"]}
            data.update({ids: data_form})

        str_data = json.dumps(data)
        return str_data

    def login(self, data_list):
        space = " "
        toReturn = ""
        collection = self.database.user_info()

        try:
            for i in collection.find({}, {'_id': 0}):

                if i['Email'] == data_list[1] and i['Password'] == data_list[2]:
                    # print(i["Email"], i["Password"])

                    toReturn: str = (
                                "login" + space + i['Email'] + space + i['Password'] + space + str(i['Name']) + space +
                                i['Phone'] + space + str(i['Deposit']))
                    # print("Log In Information Found!", toReturn)

        except Exception as err:
            print(err)
            toReturn = "Database checking Error"

        return toReturn

    def auction_check(self, data_list):
        collection = self.database.user_info()
        deposit = 0

        for i in collection.find({}, {"Email": 1, "Deposit": 1}):
            if data_list[1] == i["Email"]:
                point = i["Deposit"]
        toReturn = data_list[0] + ' ' + str(deposit)
        print(deposit, "from server side")
        return toReturn

    def register(self, data_list):
        collection = self.database.user_info()

        for i in collection.find({}, {"Email": 1, "Password": 1}):
            if data_list[1] == i["Email"] and data_list[2] == i["Password"]:
                return "This email is already registered\nPlease try again."

        data_to_update = {"Name": data_list[3], "Email": data_list[1], "Password": data_list[2],
                          "Phone": data_list[4], "Deposit": data_list[5]}

        collection.insert_one(data_to_update)

        return "success"

if __name__ == '__main__':
    auction_server = Auction_Server()

    auction_server.main()
