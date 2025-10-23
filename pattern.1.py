n = int(input("ENnter num : "))


for i in range(1,n):
    for j in range(1,(2*n - 1)):
        if(j >  ((i/2))):
            print("*")
        else:
            print(" ")
    print("\n")
    
    
