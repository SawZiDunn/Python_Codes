def usd(thb):
    print("USD \t\t", thb//36.33, "\t\t\t", thb//36.4)


def mmk(thb):
    print("MMK \t\t", thb//0.011, "\t\t\t", thb//0.016)


def jap(thb):
    print("JAP \t\t", thb//0.2525, "\t\t\t", thb//0.254)


def eur(thb):
    print("JAP \t\t", thb//36.3, "\t\t\t", thb//36.4)


def cny(thb):
    print("CNY \t\t", thb//5.23, "\t\t\t", thb//5.26)


def main():
    thb = eval(input("THB Currency :",))
    print("Currency\t Buying Rate\t\t\t Selling Rate")
    usd(thb)
    mmk(thb)
    jap(thb)
    eur(thb)
    cny(thb)


main()
    
