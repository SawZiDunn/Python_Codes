def work_hour():
    try:
        employee_num = eval(input("How many employees you want to calculate?"))

        employee_count = 1
        total = 0
        for i in range(employee_num):

            print("Employee", employee_count, ":")
            day = eval((input("How many days?")))
            employee_count += 1

            sum1 = 0
            for j in range(day):
                hour = eval(input("Hours?"))
                sum1 = sum1 + hour  # for each employee

            total += sum1
            print("Employee", employee_count - 1, "'s total paid hours =", sum1)
    except (ValueError, NameError):
        print("You must enter numbers only!")
        work_hour()

        print("============")
    print("\n======================================")
    print("Total paid hours for all employees =", total)
        
        
if __name__ == '__main__':
    work_hour()
        
