import socket
import json


class Tcp_client:

    def __init__(self, sms):
        self.target_ip = "localhost"
        self.target_port = 9998
        self.input_checking(sms)

    def run_client(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_ip, self.target_port))

        return client  # to send and receive data

    def input_checking(self, sms):
        if sms == "gad":
            self.getting_all_data(sms)

        elif sms == "login":
            self.client_log_in(sms)

        elif sms == "register":
            self.register()
        else:
            print("Invalid Option")

    def getting_all_data(self, sms):
        client = self.run_client()
        sms = bytes(sms, 'utf-8')
        client.send(sms)
        received_data = client.recv(4096)
        data_dict: dict = json.loads(received_data.decode('utf-8'))
        print(data_dict, type(data_dict))

        client.close()

    def client_log_in(self, info):
        try:
            print("This is log-in section.")
            l_email = input("Enter your email to log in:")
            l_password = input("Enter your password:")

            client = self.run_client()
            sms = info + ' ' + l_email + ' ' + l_password
            sms = bytes(sms, 'utf-8')
            client.send(sms)
            received_data = client.recv(4096)
            user_info: dict = json.loads(received_data.decode('utf-8'))

            self.option_choice(user_info, client)

            client.close()

        except Exception as err:
            print(err)

    def option_choice(self, user_info, client):
        print("Email: " + user_info["Email"])
        print("Info: " + user_info["Info"])
        print("Point: " + str(user_info["Point"]))

        try:
            option = int(input("Press 1 to get to User Option\nPress 2 to get to Main Option\nPress3 to Exit"))
            if option == 1:
                self.user_option(user_info, client)
            elif option == 2:
                pass
            elif option == 3:
                exit(1)
            else:
                print("Invalid Option")
                self.option_choice(user_info, client)
        except Exception as err:
            print(err)

    def user_option(self, user_info, client):
        try:
            option = int(input("Press 1 to Vote\nPress 2 to get more points\nPress 3 to transfer points\nPress 4 to "
                               "get Voting Ranking\nPress 5 to change user information\nPress 6 to Delete "
                               "Account\nPress 7 to Exit"))

            if option == 1:
                self.voting()

            else:
                print("Invalid Option!")
                self.user_option(user_info, client)

        except Exception as err:
            print(err)
            self.user_option(user_info, client)

    def register(self):
        print("\nThis is registration option ")
        r_email = ''
        while True:
            r_email = input("Enter email for registration :")
            flag = self.email_checking(r_email)  # 1 or -1

            if flag == 1:
                break
            else:
                print("Email Form Invalid\nTry Again! ")

        print("Email From Valid ")

        try:
            option = input("Press 1 Registration for Voter:\nPress 2 Registration for Candidate!:")

            if option == '1':
                self.reg_for_voter(r_email)
            elif option == '2':
                pass

            else:
                self.register()
        except Exception as err:
            print(err)

    def email_checking(self, r_email):
        name_counter = 0
        for i in range(len(r_email)):
            if r_email[i] == '@':
                # print("Name End Here")
                break
            name_counter += 1

        print("Name counter: ", name_counter)

        email_name = r_email[0:name_counter]
        email_form = r_email[name_counter:]

        # print(email_name)
        print(email_form)

        # checking for name
        name_flag = 0
        email_flag = 0
        for i in range(len(email_name)):
            a_char = email_name[i]
            if (31 < ord(a_char) < 48) or (57 < ord(a_char) < 65) or (
                    90 < ord(a_char) < 97) or (122 < ord(a_char) < 128):
                name_flag = -1
                break

        domain_form = ["@facebook.com", "@ncc.com", "@mail.ru", "@yahoo.com", "@outlook.com", "@apple.com", "@zoho.com",
                       "@gmail.com"]

        for i in range(len(domain_form)):

            if domain_form[i] == email_form:
                email_flag = 1
                break

        if name_flag == -1 or email_flag == 0:
            return -1

        else:
            return 1

    def reg_for_voter(self, r_email):

        if self.email_check_in_database(r_email):
            try:
                pass1 = input("Enter your password to register:")
                pass2 = input("Enter your password Again  to register:")

                if pass1 == pass2:

                    print("Passwords match!")
                    phone = int(input("Enter your phone number:"))

                    data_list = [r_email, pass1, phone]
                    self.final_registration(data_list)

                else:
                    print("Password not match:")
                    self.reg_for_voter(r_email)

            except Exception as err:
                print(err)

        else:

            print("Your email was already register!")
            self.register()

    def email_check_in_database(self, email):

        client = self.run_client()
        data_to_send = "emailcheck" + " " + email

        client.send(bytes(data_to_send, "utf-8"))

        received = client.recv(4096).decode("utf-8")

        print(received)

        if received == "notExist":
            client.close()
            return True
        else:
            client.close()
            return False

    def final_registration(self, data_list):

        data_form = "register" + " " + data_list[0] + " " + data_list[1] + " " + str(
            data_list[2]) + " " + "User" + " " + "100"

        client = self.run_client()

        client.send(bytes(data_form, "utf-8"))

        recv = client.recv(4096).decode("utf-8")

        print(recv)

        if recv:
            print("Registration Success!", recv)
            info = "login"
            self.client_log_in(info)

        client.close()

    def voting(self):

        client = self.run_client()

        sms = bytes("Candidate_Info", 'utf-8')
        client.send(sms)
        info = client.recv(4096)
        candidate_info: dict = json.loads(info.decode('utf-8'))

        for i in candidate_info:
            print("No." + str(i) + " Name:" + candidate_info[i]["Name"] + " Voting_Point:" +
                  str(candidate_info[i]["Voting_Point"]))

            voted_candidate = input("Enter the number of the candidate you want to vote:")

            data_to_send = "vote " + voted_candidate
            client = self.run_client()

            client.send(bytes(data_to_send, 'utf-8'))
            client.recv(4069)

        client.close()


if __name__ == '__main__':

    while True:
        data: str = input("Enter some data to send :")
        tcp_client = Tcp_client(data)
