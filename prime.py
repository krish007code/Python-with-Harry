num = int(input("number to check : "))
for i in range(2,num - 1):
    if(num % i )== 0:
        print("not prime")
        break 
else:
    print("prime")