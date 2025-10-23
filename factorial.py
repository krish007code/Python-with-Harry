n = int(input("number to check : "))
sum = 1
for i in range(1,n):
    sum = sum * (i+1)
    i += 1
print(sum)