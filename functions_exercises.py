def find_largest():
    lists = [100, 5, 6, 4, 7, 8, 9, 5, 4, 1, 2, 5, 8, 7, 4, 58, 9, 59]
    largest_num = 0
    for i in range(len(lists)):
        if lists[i] >= largest_num:
            largest_num = lists[i]
    print(f"The largest number in the list is {largest_num}.")


def find_smallest():
    lists = [6, 4, 7, 6, 5, 5, 4, 1, -5, 2, 5, 8, 7, 4, 58, 9]
    smallest_num = lists[0]

    for i in lists:
        if i < smallest_num:
            smallest_num = i
    print(f"The smallest number in the list is {smallest_num}.")


def future_investment():
    deposit = eval(input("How much is your deposit now?"))
    interest_rate = eval(input("Put the interest rate:"))
    n=eval(input("How many years will you wait?"))

    for i in range(n):
        deposit = deposit+(deposit/100*interest_rate)
        print(deposit)
    print("Total_Deposit =", deposit)


def duplication_remove():
    lists = [6, 4, 7, 6, 5, 5, 4, 4, 4, 5, 6, 4, 5]
    new_lists = []

    for num in lists:
        if num not in new_lists:
            new_lists.append(num)
    print(new_lists)


def num_interpret():
    x = input("Input your phone number:")
    y = ""
    digits = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
    }

    for i in x:
        y += digits.get(i, "!") + " "
    print(y)


def exception_handling():
    try:
        age = int(input("Enter your age :"))
        income = 2000
        risk = income / age
        print(f"Your age is {age}.")
    except ValueError:
        print("Invalid Value")
    except ZeroDivisionError:
        print("Try except Zero")


def triangle_pattern():
    nrow = eval(input("enter number of rows: "))
    for i in range(nrow):
        for j in range(i+1):
            print(j+1, end=" ")
        print("\n")


def is_prime(num):
    if num < 2:
        return False
    else:
        for temp in range(2, num):
            if num % temp == 0:
                return False
    return True


def next_prime(num):
    num0 = num
    while True:
        num += 1
        if is_prime(num):
            letter = f"{num0} is no prime.\nThe next prime number is {num}."
            return letter


def main_prime_check():
    num = int(input("Enter a number :"))
    if is_prime(num):
        return True
    else:
        return next_prime(num)


def printer():
    a = 10
    b = 50
    c = 1.2354658

    print(f"{a} is less than {b}")

    print("{1} is greater than {0}".format(a, b))

    print("Hello {name}, Welcome to {an} {num}.".format(name="ZiDunn", an="Golden Land", num=37))

    print("The value of c is %.2f." % c)