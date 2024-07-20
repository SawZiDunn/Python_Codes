def d():
    animal = "elephant"
    def e():
        nonlocal animal
        animal = "tiger"
        print("Inside nested function:" + animal)
    print("Before calling function: " + animal)
    e()
    print("After calling function: " + animal)
    
animal = "panda"
d()
print("Global animal: " + animal)
