num1 = int(input("Enter the marks :"))
num2 = int(input("Enter the marks :"))
num3 = int(input("Enter the marks :"))

percentage = (num1 + num2 + num3)/300

if( percentage > 40 and num1 > 33 and num2 > 33 and num3 > 33):
    print("you passed")
else:
    print("you failed")