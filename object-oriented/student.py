class Student:
    def __init__(self, name, clan):

        self.name = name
        self.clan = clan


def main():
    student = get_student()
    print(f"{student.name} from {student.clan} Clan")


def get_student():
    name = input("Name: ")
    clan = input("Clan: ")

    student = Student(name, clan)

    return student


if __name__ == '__main__':
    main()