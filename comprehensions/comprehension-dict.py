# dict = { key:value for key, value in <sequence> if <condition> }
# new_dict ={key:value for (key, value) in zip(list1, list2)} # for two lists

students = ["Naruto", "Nagato", "Karin"]

# creating a dictionary from a list
uzumaki_members: list = [
    {"name": student, "clan": "Uzumaki"} for student in students
]

uzumaki: dict = {student: "Uzumaki" for student in students}
print(uzumaki)

for i, student in enumerate(students):
    print(i, student)
    
# Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)