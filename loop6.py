num = int(input("Enter the num : "))
for i in range(1,num + 1):
    print(" "*(num - i), end= "")
    print("*"*(2 * i - 1), end= "")
    print("\n")
    
