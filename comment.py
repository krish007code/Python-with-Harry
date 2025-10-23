comment =  input("Enter the text\n")
'''if( comment.find("Make a lot of money") != -1 or comment.find("buy now") != -1 ):
    print("TExt is spam")
else:
    print("not spam")'''
if("MAke a lot of money" in comment or "buy now" in comment):
    print("spam")
else:
    print("not spam")
