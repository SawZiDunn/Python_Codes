import re


def format():
    name = input("Name: ").strip()

    if matches := re.search(r"^(.+), *(.+)?", name):  # get return value first, then check if it's true
        last, first = matches.groups()  # to use with the return value of re.search()
        # or
        # last = matches.group(1)  # index starts from 1
        # first = matches.group(2)

        print(f"{first} {last}")