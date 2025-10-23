letter = '''
       Dear <|Name|>,
       You are selected!
       <|Date|>
       '''
name  = str(input("Enter name : "))
date  = str(input("Enter date : "))
print(letter.replace( "|Name|", name).replace("|Date|", date))
