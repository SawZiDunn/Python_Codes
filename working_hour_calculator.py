def work_hour():
    employee_num=eval(input("How many employees you want to calculate?"))
    a=1
    a0=1
    sum=0
    for i in range (employee_num):
        
        print("Employee" ,a , ":")
        day=eval((input("How many days?")))
        a+=1
        
        sum1=0     
        for j in range (day):
            
            hour=eval(input("Hours?"))
            sum1=sum1+hour
            

        sum=sum+sum1
        print("Employee", a0, "'s total paid hours =", sum1)
        a0=a0+1
        print("============")
    print("\n======================================")
    print("Total paid hours for all employees =", sum)
        
        
work_hour()
        
