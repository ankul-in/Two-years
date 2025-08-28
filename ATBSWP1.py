#ATBSWP automate the boring stuff with python
#finding pattern of text without regular expressions
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
        if text[3] != "-":
            return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
        if text[7] != "-":
            return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
phonenumber=input("enter your phone number to check its validity-->")
#americal phone numbers
print(isPhoneNumber(phonenumber))
