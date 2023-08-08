import socket
import client_encryp_decrip


class Auction_client:

    def __init__(self):
        self.target_ip = "localhost"
        self.target_port = 9998
        self.key = self.get_key()


    def run_client(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_ip, self.target_port))

        return client

    def get_key(self):
        key = input("Enter your key for encryption:")
        return key

    def client_menu(self):
        client = self.run_client()
        option = eval(input("Press 1 to log in\nPress 2 to register\nPress 3 to exit"))

        if option == 1:
            self.log_in(client)

        elif option == 2:
            self.register(client)
        elif option == 3:
            exit(1)
        else:
            print("Invalid Option")
            self.client_menu()

    def log_in(self, client):
        space = ' '
        logIn_email = ""
        logIn_password = ""

        try:
            logIn_email = input("Enter your user email to Log in:")
            logIn_password = input("Enter your password:")

        except Exception as err:
            print("Invalid Input\n", err)
            self.client_menu()

        raw_data = 'login' + space + logIn_email + space + logIn_password

        decrypted_data_from_server = self.sending_encrypted_data(raw_data, client)

        decrypted_data_from_server = decrypted_data_from_server.split(' ')

        if decrypted_data_from_server[0] == 'login' and decrypted_data_from_server[1] == logIn_email and \
                decrypted_data_from_server[2] == logIn_password:
            print("Login Successful")
            self.user_main_menu(decrypted_data_from_server)

        else:
            print("Login Failed")
            print(decrypted_data_from_server)
            self.client_menu()

    def register(self, client):
        raw_data: str = "register "
        register_email: str = input("Enter your email to register:")
        register_password0: str = input("Enter your password to register:")
        register_password1: str = input("Confirm your password:")

        if register_password0 != register_password1:
            print("Password Confirmation Failed!\nPlease try again.")
            self.register(client)

        register_name: str = input("Enter your name:")

        register_name = register_name.replace(' ', '_')

        register_ph_num: str = input("Enter your phone number:")
        while True:
            deposit_amount: int = int(input("Enter your deposit amount (Minimum: 3000 Baht"))
            if deposit_amount < 3000:
                print("You must deposit at least 3000 Baht!")
            else:
                break

        raw_data += (register_email + ' ' + register_password0 + ' ' + register_name + ' ' + register_ph_num + ' ' +
                     str(deposit_amount))

        received_data = self.sending_encrypted_data(raw_data, client)
        if received_data == "success":
            self.client_menu()
        else:
            print(received_data)
            self.client_menu()

    def user_main_menu(self, data_from_server):
        client = self.run_client()
        space = ' '
        option = eval(input("Press 1 to get the info of all products\nPress 2 to make deposit\nPress 3 to transfer "
                            "money\nPress 4 to start auction\nPress 5 to exit"))

        if option == 1:
            self.sending_encrypted_data("info", client)
        elif option == 2:
            print("This is for adding points")

        elif option == 3:
            print("This is for transferring points")

        elif option == 4:

            raw_message = "auction" + space + data_from_server[1]
            # print("This is raw_message to send from option 4: ", raw_message)
            received_data = self.sending_encrypted_data(raw_message, client)

            received_data = received_data.split(' ')  # splitting received data
            # print("This is received back data from server in option 4: ", received_data)

            try:
                print("Auction starts here!")

            except Exception as err:
                print(err)
                print("Error at option 4 received_data checking!")
                self.user_main_menu(data_from_server)

        elif option == 5:
            self.client_menu()
        else:
            print("Invalid Option")
            self.user_main_menu(data_from_server)

    def sending_encrypted_data(self, data_to_send: str, client):
        # print("This is data to send from sending_encrypted_data function:", data_to_send)

        encryption = client_encryp_decrip.A3_Encryption()
        decryption = client_encryp_decrip.A3_Decryption()

        encrypted_data: str = encryption.start_encryption(data_to_send, self.key)

        client.send(bytes(encrypted_data, 'utf-8'))

        # print("already sent from client")
        received_info = client.recv(4096).decode('utf-8')
        # print("already received from client")

        decrypted_data = decryption.start_decryption(received_info)
        print("This is decrypted data received back from server: ", decrypted_data)
        return decrypted_data


if __name__ == '__main__':
    auction_client = Auction_client()

    while True:

        auction_client.client_menu()
