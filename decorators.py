def modify(f):
    def wrapper():
        print("This is modify function")
        f()
        print("Modification Complete!")
    return wrapper


# modify function takes hello() as a parameter and modify it to a new function()
@modify
def hello():
    print("Hello World")


hello()