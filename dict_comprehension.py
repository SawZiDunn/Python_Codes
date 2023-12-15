students = ["Naruto", "Nagato", "Karin"]

# uzumaki: list = [
#     {"name": student, "clan": "Uzumaki"} for student in students
# ]

uzumaki: dict = {student: "Uzumaki" for student in students}

print(uzumaki)

for i, student in enumerate(students):
    print(i + 1, student)