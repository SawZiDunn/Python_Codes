import sys

class Voting:
    def __init__(self):
        self.participants = {0: {"name": "Ronaldo", "votes": 0, "voters": []},
                             1: {"name": "Messi", "votes": 0, "voters": []},
                             2: {"name": "Benzema", "votes": 0, "voters": []},
                             3: {"name": "Vinicius", "votes": 0, "voters": []},
                             4: {"name": "Ronaldinho", "votes": 0, "voters": []},
                             5: {"name": "Rushford", "votes": 0, "voters": []}}
        self.db: dict = {}
        self.id: int = 0
        self.login_id = 0

    def main_option(self):
        option = 0

        try:
            option = eval(input("Press 1 to register\nPress 2 to log in\nPress 3 to exit"))

        except ValueError:
            print("Please insert only integer!\n")
            self.main_option()

        if option == 1:
            self.register()

        elif option == 2:
            self.log_in()

        elif option == 3:
            sys.exit()

        else:
            print("Invalid Option\n")
            self.main_option()

    def register(self):
        try:
            register_email = input("Enter your email to register :")

            while True:
                register_password0 = input("Enter your password to register :")
                register_password1 = input("Confirm your password :")

                if register_password0 != register_password1:
                    print("Incorrect Password Confirmation!\n")
                else:
                    break

            register_name = input("Enter your name :")
            point = 0
            point = int(point)

            print("You need to purchase points before voting.\n")

            while True:
                try:
                    deposit_amount = eval(input("Enter your deposit amount (minimum 5000 Baht) :"))
                    if deposit_amount >= 5000:
                        break
                    else:
                        print("The minimum deposit should be not less than 5000 Baht.")

                except Exception as err:
                    print(err)

            self.id = len(self.db)
            data_form: dict = {
                self.id: {"Email": register_email, "Password": register_password0, "Name": register_name,
                          "Deposit_amount": deposit_amount, "Point": point}}

            self.db.update(data_form)

            print("Registration Successful!\n")
            self.main_option()

        except Exception as err:
            print(err)
            self.register()

    def log_in(self):

        db_length = len(self.db)
        self.login_id = -1

        try:
            login_email = input("Enter your email :")
            login_password = input("Enter your password :")

            for i in range(db_length):
                if self.db[i]["Email"] == login_email and self.db[i]["Password"] == login_password:
                    print("Log_in Successful!\n")

                    self.login_id = i
                    self.user_sector()

                else:
                    print("Please try again!")
                    self.log_in()

        except Exception as err:
            print(err, "\nPlease try again!")

    def user_sector(self):
        print("Welcome, Mr.", self.db[self.login_id]["Name"], "...")

        if self.db[self.login_id]["Point"] == 0:
            print("You have no point to vote")
        else:
            print(f'You have {self.db[self.login_id]["Point"]} to vote.')

        try:
            option = eval(input("Press 1 to vote\nPress 2 to purchase points\nPress 3 to check balance\n"
                                "Press 4 to top-up\nPress 5 to return to main option\nPress 6 to exit:\n"))

            if option == 1:
                self.voting()
            elif option == 2:
                self.purchase_point()
            elif option == 3:
                print(f"Your balance is {self.db[self.login_id]['Deposit_amount']} Baht.")
                self.user_sector()
            elif option == 4:
                self.top_up_deposit()

            elif option == 5:
                self.main_option()
            elif option == 6:
                exit(1)
            else:
                print("Incorrect option!\nPlease try again!\n")
                self.user_sector()
        except Exception as err:
            print(err, "\n")
            self.user_sector()

    def top_up_deposit(self):
        amount = eval(input("Enter your top-up amount: "))
        if amount < 500:
            print("You top-up amount should be not less than 500 Baht.")
            self.top_up_deposit()
        else:
            self.db[self.login_id]['Deposit_amount'] += amount
            print(f"You have topped up {amount} Baht to your account.")
            self.user_sector()

    def purchase_point(self):
        print(f"Your balance is {self.db[self.login_id]['Deposit_amount']} Baht.")
        print("1 point to vote = 500 Baht")
        try:
            points = eval(input("How many points you want to buy? :"))
            total_amount = points * 500

            if total_amount > self.db[self.login_id]['Deposit_amount']:
                print("Insufficient Balance!")

                while True:
                    option = eval(input("Press 1 to top-up\nPress 2 to return to user sector\nPress 3 to exit"))
                    if option == 1:
                        self.top_up_deposit()
                    elif option == 2:
                        self.user_sector()
                    elif option == 3:
                        exit(1)
                    else:
                        print("Invalid Option!")

            else:
                self.db[self.login_id]['Deposit_amount'] - total_amount
                self.db[self.login_id]['Point'] += points
                print(f"You have successfully purchased {points} points.")
                self.user_sector()

        except Exception as err:
            print(err)
            self.purchase_point()

    def voting(self):
        for i in range(len(self.participants)):
            print("ID: {} - Name: {} - Current Votes: {}".format(i, self.participants[i]["name"],
                                                                 self.participants[i]["votes"]))

        try:
            choice = eval(input("Please vote for the participant by choosing an ID number."))

            self.participants[choice]["votes"] += 1
            self.participants[choice]["voters"].append(self.db[self.login_id]["Name"])

            if self.db[self.login_id]["Point"] == 0:
                self.user_sector()
            else:
                self.db[self.login_id]["Point"] -= 1

            print("Congratulations!\nYou have successfully voted.\n")

            for i in range(len(self.participants)):
                print("ID: {} - Name: {} - Current Votes: {} - Voters: {}".format(i, self.participants[i]["name"],
                                                                                  self.participants[i]["votes"],
                                                                                  self.participants[i]["voters"]))

            self.user_sector()

        except Exception as err:
            print(err)
            self.user_sector()

    def recording_data_to_file(self):
        pass

    def loading_data_from_file(self):
        pass
