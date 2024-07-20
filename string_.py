def main():
    x = eval(input("Which number of month do you like? - "))
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    month_index = (x - 1) * 3
    month_name = months[month_index: month_index + 3]
    print(month_name)


def main4():
    a = "How", "are", "you?"
    
    x = ".".join(a)
    print(x)
    
def string_reverse(str):
    return str[:: -1]

def string_reverse_recursive(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse_recursive(str[1:]) + str[0]


print(string_reverse_recursive("Hello World"))
