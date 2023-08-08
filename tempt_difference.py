def main():
    file_name = input("What file are the temperature in? ")
    infile = open(file_name, 'r')
    line = infile.readline()

    temp = 0
    count = 0
    for number in line.split(' '):
        in_number = eval(number)
        if count == 0:
            temp = in_number
        else:
        #elif count >= 1:
            differ = in_number - temp
            if temp < in_number:
                print(differ, "HOTTER")
            else:
                print(differ, "COOLER")
            temp = in_number
        count = count + 1


main()
