import re


def main():
    email = input("Email: ").strip()
    #  "\w" means [a-zA-Z0-9_]
    #  "+" means one or more of its left char
    #  "\s" is a whitespace

    if re.search(r"^\w+@gmail.com$", email, re.IGNORECASE):
        print("Valid")
    else:
        print("Invalid")


if __name__ == '__main__':
    main()