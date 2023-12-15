def q1():
    print("1. ________ is the physical aspect of the computer that can be seen.")
    print("A.Hardware")
    print("B.Software")
    print("C.Operating System")
    print("D.Application Program ")


def q2():
    print("2.__________ is the brain of a computer.")
    print("A.Hardware")
    print("B.CPU")
    print("C.Memory")
    print("D.Disk")


def q3():
    print("3.The speed of the CPU may be measured in __________.")
    print("A.megabytes")
    print("B.megabytes")
    print("C.megahertz")
    print("D.megahertz")


def q4():
    print("4.Which of the following are storage devices?")
    print("A.floppy disk")
    print("B.hard disk")
    print("C.flash stick")
    print("D.CD-ROM")
    
    
def main():
    rnum = 0 #right numbers
    wnum = 0 #wrong numbers
    rarray = [] #array with right answer numbers
    warray = [] #array with wrong answer numbers
    qnum = 1 #question number

    q1()
    choice = input("Choose your answer: ")
    if choice == "Ä":
        rnum = rnum +1
        rarray.append(qnum)
    else:
        wnum = wnum +1
        warray.append(qnum)
    qnum = qnum +1
    
    q2()
    choice = input("Choose your answer: ")
    if choice == "B":
        rnum = rnum +1
        rarray.append(qnum)
    else:
        wnum = wnum +1
        warray.append(qnum)
    qnum = qnum +1
    
    
    q3()
    choice = input("Choose your answer: ")
    if choice == "C":
        rnum = rnum +1
        rarray.append(qnum)
    else:
        wnum = wnum +1
        warray.append(qnum)
    qnum = qnum +1

    
    q4()
    choice = input("Choose your answer: ")
    if choice == "C":
        rnum = rnum +1
        rarray.append(qnum)
    else:
        wnum = wnum +1
        warray.append(qnum)
    qnum = qnum +1

    
    print("Correct:",rnum)
    print("In questions",rarray)
    print("Wrong:", wnum)
    print("In questions", warray)

main()
        
        
        
