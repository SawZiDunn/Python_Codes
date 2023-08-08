def main():
    count = 0
    count1 = 0
    
    fname = input ("What is the file name to take the data from?")
    infile = open (fname, "r")
    line = infile.readline()
    
    for temp in line.split (" "):   #temp = current temperature
        count = count + 1
        temp = int(temp)
        if count == 1:
            pretemp = temp  #pretemp = previous temperature

        else:
            count1=count1+1
            td = temp - pretemp    #td = temperature difference
            if td > 0:               
                print ("Day",count1,": Temperature changed by", td, "Degree Celcius: HOTTER")

            else:
                print ("Day", count1, ": Temperature changed by", td, "Degree Celcius: COOLER")
            pretemp = temp
            
main()
