def calculator():
    x = int(input("enter any number"))
    y = int(input("enter any number"))
    z = input("choose A, B, C, D for addition, subtraction, multiplication and division")

    if (z=="A"):
        print(x+y)
    elif(z=="B"):
        print(x-y)
    elif(z=="C"):
        print(x*y)
    elif(z=="D"):
        print(x/y)
    else:
        print("Invalid operation choice. Please choose A, B, C, or D.") 

calculator()