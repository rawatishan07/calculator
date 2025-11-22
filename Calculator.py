def calculator():
    x = int(input("enter any number"))
    y = int(input("enter any number"))
    z = input("choose A, B, C, D for addition, subtraction, multiplication and division")

    if (z=="A"):
        print(x+y)
    elif(z=="B"):
        print(x-y)