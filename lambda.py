students = [
    {"name": "Naruto", "clan": "Uzumaki"},
    {"name": "Nagato", "clan": "Uzumaki"},
    {"name": "Sasuke", "clan": "Uchiha"},
    {"name": "Karin", "clan": "Uzumaki"}
]


# uzumaki = [
#     student["name"] for student in students if student["clan"] == "Uzumaki"
# ]


# def is_uzumaki(student_dict_list):
#     return s["clan"] == "Uzumaki"


uzumaki_list = filter(lambda student_list: student_list["clan"] == "Uzumaki", students)

for each in sorted(uzumaki_list, key=lambda student_dic_list: student_dic_list["name"]):
    print(each["name"])
