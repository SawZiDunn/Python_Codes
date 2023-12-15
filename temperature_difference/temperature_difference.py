def main():
    previous_temp = 0
    count = 0
    day_count = 0
    
    file_name = input("What is the file name to take the data from?")  # temperature.txt
    infile = open(file_name, "r")
    line = infile.readline()
    
    for temp in line.split(" "):   # temp = current temperature
        count = count + 1
        temp = int(temp)
        if count == 1:
            previous_temp = temp

        else:
            day_count = day_count + 1
            td = temp - previous_temp    # td = temperature difference
            if td > 0:               
                print("Day", day_count, ": Temperature changed by", td, "Degree Celsius: HOTTER")

            else:
                print("Day", day_count, ": Temperature changed by", td, "Degree Celsius: COOLER")
            previous_temp = temp


main()
