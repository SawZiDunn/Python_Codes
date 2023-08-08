def loop():
    count = 0
    total = 0
    file = input("Type the file name...")
    opened_file = open(file, "r")

    # only for files with one number in each line(can have multiple lines) eg. "a.txt"

    for line in opened_file.readlines():
        count = count + 1
        total += int(line)
    print("The average is", total / count)


def loop1():
    count = 0
    total = 0
    file = input("Type your file name")
    infile = open(file, "r")
    line = infile.readline()

    # basically the same with loop()

    while line != "":
        count = count + 1
        total = total + eval(line)
        line = infile.readline()
    print("The average is", total / count)


def loop2():
    filepath = input("What file are the numbers in? ")

    with open(filepath) as file:
        line = file.readline()
        total = 0
        count = 1

    while line:
        print("Line {}".format(line.strip()))
        line = file.readline()

        if line.strip():
            n = int(line)
            total = total + n
            count = count + 1

        print("\nThe average of the numbers is", total / count)


def loop3():
    total = 0
    count = 0
    filename = input("Type your file name")
    infile = open(filename, "r")
    line = infile.readline()

    # for files with multiple numbers in one line separated by something(can have multiple lines)
    # eg. "b.txt"

    while line != "":
        for x in line.split(","):
            total = total + eval(x)
            count = count + 1
        line = infile.readline()
    print(total)
    print("The average number is", total / count)


loop2()
