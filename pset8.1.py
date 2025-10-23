
def greatest():
    num1 = int(input("Enter the num : "))
    num2 = int(input("Enter the num : "))
    num3 = int(input("Enter the num : "))
    if num1 > num2 and num1 > num3 :
        return num1
    elif num2 > num1 and num2 > num3 :
        return num2
    elif num3 > num2 and num1 < num3 :
        return num3
    else:
        return None
    

print(greatest())