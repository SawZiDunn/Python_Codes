def main():
    yell("This", "is", "CS50.")


def yell(*words):
    # for word in words:
    #     uppercased.append(word.upper())

    # uppercased = map(str.upper, words)  # using upper() method from str class to every word in words

    uppercased = [word.upper() for word in words]  # list comprehension
    print(*uppercased)


if __name__ == '__main__':
    main()