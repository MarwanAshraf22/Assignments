while True :
    OP=input("Please enter the operation you want (add,sub,mult,div) : ")
    if (OP!="add" and OP!="sub" and OP!="mult" and OP!="div") :
        print("There is no such an operation")
        continue
    x=float(input("Please enter the first number : "))
    y=float(input("Please enter the second number : "))
    if (OP=="add") :
        from calc import add
        print(add(x,y))
    elif (OP=="sub") :
        from calc import sub
        print(sub(x,y))
    elif (OP=="mult") :
        from calc import mult
        print(mult(x,y))
    elif (OP=="div") :
        from calc import div
        print(div(x,y))

    z=input("Do you want to do another operation ? if yes type yes if no type no : ")
    if z == "yes":
        continue
    else:
        break