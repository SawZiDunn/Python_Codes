def irs111(credit1,grade1):
    print("IRS111\t\t\t", credit1, "\t\t", grade1)
    a = credit1*grade1
    return a


def irs131(credit2,grade2):
    print("IRS131\t\t\t", credit2,"\t\t", grade2)
    b=credit2*grade2
    return b


def irs183(credit3,grade3):
    print("IRS183\t\t\t", credit3,"\t\t", grade3)
    c=credit3*grade3
    return c


def irs112(credit4,grade4):
    print("IRS112\t\t\t", credit4,"\t\t", grade4)
    d=credit4*grade4
    return d


def gpa_calculator():
    print("Notice that all subjects have 3 credits each.")
    credit1,grade1=eval(input("Put your GPÄ and Grade for irs111 :"))
    credit2,grade2=eval(input("Put your GPÄ and Grade for irs131 :"))
    credit3,grade3=eval(input("Put your GPÄ and Grade for irs183 :"))
    credit4,grade4=eval(input("Put your GPÄ and Grade for irs112 :"))

    print("Subject Code\t\tCredit\t\tGrade")
    A=irs111(credit1,grade1)
    B=irs131(credit2,grade2)
    C=irs183(credit3,grade3)
    D=irs112(credit4,grade4)

    print("\t\tGPA  =\t", (A+B+C+D)/12)


gpa_calculator()
