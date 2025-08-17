#change all numbers in file to text
def numToText(num):
    numToText={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
    return "".join(numToText[digit] for digit in str(num) if digit in numToText)
def convertNumToText(file_path):
    with open(file_path,"r") as file:
        content=file.read()
    modifiedContent="".join(numToText(int(c) if c.isdigit() else c for c in content))
    with open(file_path,"w") as file:
        file.write(modifiedContent)
file_path="example.txt"
convertNumToText(file_path)
print("numbers converted to text in the file")