def withdraw():
    wmon = eval(input("How much money do you want to withdraw?"))
    print("You have withdrawn ", wmon, "Baht.")

def deposit():
    deposit = 10000
    
    return deposit

def e_funds():
    return "e_funds"

def balance():
    return "balance"


def main():
    print("You have five options. \n 1.Withdraw \n 2.Deposit \n 3.E-funds \n 4.Balance \n 5.Quit")
    A = withdraw()
    B = deposit()
    C = e_funds()
    D = balance()
    nchoice = eval(input("What do you wish to do, Sir?\n Choose No.1 to 5: "))
    for i in range(30):
        if nchoice <= 4:
            if nchoice == 1:
                print(A)
            if nchoice == 2:
                print("Your deposit is", B, " Baht.")
            if nchoice == 3:
                print(C)
            if nchoice == 4:
                print(D)
            nchoice = eval(input("What do you wish to do next, Sir?\n Choose No.1 to 5: "))
        else:
            print("Thanks for using our bank systme.")
            break
