def main():
    x = eval(input("Which number of month do you like? - "))
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    month_index = (x - 1) * 3
    month_name = months[month_index: month_index + 3]
    print(month_name)


def main2():
    x = input("Type the message which will be converted into unicode - ")
    for ch in x:
        print(ord(ch), end=" ")


def main3():
    x = (input("Add the codes you want to convert into characters - "))
    z = ""
    for i in x.split(" "):
        y = int(i)
        z += chr(y)
    print(z)


def main4():
    a = "How", "are", "you?"
    x = ".".join(a)
    print(x)


main4()
