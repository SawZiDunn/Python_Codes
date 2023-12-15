def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


def unpack():
    coins0: list = [100, 50, 25]
    coins1: dict = {"galleons": 100, "sickles": 50, "knuts": 25}

    # * for unpacking lists
    # print(total(*coins0), "knuts")
    # print(*coins0, sep=", ")

    # ** for unpacking dicts
    print(total(**coins1), "knuts")


def f(*args, **kwargs):
    # print("Positional: ", args)
    print("Name: ", kwargs)


f(galleons=100, sickles=50, knuts=25)