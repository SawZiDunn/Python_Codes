import socket
import pymongo
import json

connection = pymongo.MongoClient("mongodb+srv://ZiDunn:DgKSyyMopDlVQQBl@cluster0.diludbd.mongodb.net/", 27017)
database = connection["new_db"]
collection = database["user_info"]

collection2 = database["candidate_info"]


class Tcp_server:

    def __init__(self):
        self.server_ip = "localhost"
        self.server_port = 9998
        self.toSave = {}

    def main(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.server_ip, self.server_port))
        server.listen()
        print("Server is listening on IP: {} and Port: {}.".format(self.server_ip, self.server_port))

        try:
            while True:
                client, address = server.accept()
                print("Connection accepted from {}.".format(address))
                self.handle_client(client)
        except Exception as err:
            print(err)

    def handle_client(self, client_socket):

        with client_socket as sock:
            data_from_client = sock.recv(1024)

            data_list: list = data_from_client.decode("utf-8").split(' ')

            if data_list[0] == "gad":
                self.getting_all_data(sock)

            elif data_list[0] == "login":
                self.login_check(sock, data_list)

            elif data_list[0] == "Candidate_Info":  # don't separate the string
                self.candidate_info(sock)

            elif data_list[0] == "emailcheck":

                self.email_checking(data_list[1], sock)

            elif data_list[0] == "register":

                self.registration(data_list, sock)

            elif data_list[0] == "vote":
                pass

            else:
                sms = bytes("Invalid Option - from Server Side", 'utf-8')
                sock.send(sms)

    def getting_all_data(self, sock):
        data_dict: dict = {}

        for i in collection.find({}, {"_id": 0}):
            ids = len(data_dict)
            data_form = {"email": i["Email"], "password": i["Password"], "phone": i["Phone"]}
            data_dict.update({ids: data_form})

        str_data = json.dumps(data_dict)
        str_data = bytes(str_data, 'utf-8')
        sock.send(str_data)

    def login_check(self, sock, data_list):
        l_email = data_list[1]
        l_password = data_list[2]
        mark = -1
        sms = ""

        for i in collection.find({}, {"_id": 0, "Email": 1, "Password": 1, "Info": 1, "Point": 1}):
            if i["Email"] == l_email and i["Password"] == l_password:
                mark = 1
                sms = {"Email": i["Email"], "Info": i["Info"], "Point": i["Point"]}
                sms = json.dumps(sms)

                break

        if mark == 1:
            str_data = bytes(sms, 'utf-8')
            sock.send(str_data)
        else:
            str_data = bytes("Username and Password not found!", 'utf-8')
            sock.send(str_data)

    def candidate_info(self, sock):
        to_send = {}
        for i in collection2.find({}, {"_id": 0}):
            _id = len(to_send) + 1

            to_update = {_id: {"Name": i["Name"], "Voting_Point": i["Point"]}}
            to_send.update(to_update)

        sock.send(bytes(json.dumps(to_send), 'utf-8'))

    def email_checking(self, email, sock):
        email_exist = 0
        for i in collection.find({}, {"_id": 0, "Email": 1}):
            if i["Email"] == email:
                email_exist = 1

        if email_exist == 0:  # email not already exist
            sock.send(bytes("notExist", "utf-8"))

        else:
            sock.send(bytes("Email exists.", "utf-8"))

    def registration(self, data_list: list, sock):

        data_form = {"Email": data_list[1], "Password": data_list[2], "Phone": int(data_list[3]), "Info": data_list[4],
                     "Point": int(data_list[5])}

        ids = collection.insert_one(data_form)
        print("Registration success for :", ids.inserted_id)

        sock.send(bytes(str(ids.inserted_id), "utf-8"))


if __name__ == '__main__':
    tcp_server = Tcp_server()
    tcp_server.main()
