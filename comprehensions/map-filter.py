my_list = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def choose_number(num):
    if num > 5:
        return num
    
# new_list = map(choose_number, my_list)
# print(new_list)
# for i in new_list:
#     print(i)

# filter function return the item for which the function returns true
filter_list = filter(choose_number, my_list)
print(filter_list)
for i in filter_list:
    print(i)