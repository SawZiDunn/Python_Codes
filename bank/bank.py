def bank():
    greeting = input("Greeting:")
    dollar = 0
    if greeting.lower()[0:5] == "hello":
        dollar = 0
        print(f"${dollar}")
    
    elif greeting.lower()[0] == "h":
        dollar = 20
        print(f"${dollar}")
    else:
        dollar = 100
        print(f"${dollar}")


bank()