def temp_convert():
    c = int(input("Enter the temp : "))
    f = (c * 1.8) + 32
    return f

print(round(temp_convert(), 2))