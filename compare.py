num1 = int(input("Enter the num :"))
num2 = int(input("Enter the num :"))
num3 = int(input("Enter the num :"))
num4 = int(input("Enter the num :"))

if(num1 > num2):
    if(num1 > num3):
        if(num1 > num4):
            print(f"the number biggest is",{num1})
else:
    if(num2 > num3):
        if(num2 > num4):
            print(f"the number biggest is",{num2})
    else:
        if(num3 > num4):
            print(f"the number biggest is",{num3})
        else:
            print(f"the number biggest is",{num4})

            