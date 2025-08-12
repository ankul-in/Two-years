#test if string contain word "english" KATA 5
def checkString(string):
    word="english"
    if word in string.lower():
        return True
    else:
        return False