#atbswp
#using regular expressions
import re
x="my number is 123-456-7890."
phoneNumRegex=re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo=phoneNumRegex.search(x)
print("phone number found : "+mo.group())



#() operator
phoneNumRegex1=re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo=phoneNumRegex1.search(x)
print(mo.group(1))
print(mo.group(0))
print(mo.group())
print(mo.groups())
areacode,mainNumber=mo.groups()
print(areacode)
print(mainNumber)



heroRegex = re.compile(r"Batman|Tina Fey")
mo1=heroRegex.search(x)
mo2=heroRegex.search("Batman and Tina Fey.")
#mo1.group()
print(mo2.group())
mo3=heroRegex.search("Tina Fey and Batman.")
print(mo3.group())



#|operator
batRegex=re.compile(r"Bat(man|mobile|copter|bat)")
mo=batRegex.search("Batmobile lost a wheel")
print(mo.group())
print(mo.group(1))



#?operator
batRegex=re.compile(r"Bat(wo)?man")
mo1=batRegex.search("the Adventures of Batman")
print(mo1.group())
mo2=batRegex.search("the Adventures of Batwoman")
print(mo2.group())


#* operator
batRegex=re.compile(r"Bat(wo)*man")
mo1=batRegex.search("the adventures of Batwowowowowowowowowoman")
print(mo1.group())


greedyHaRegex=re.compile(r"(Ha){3,5}")
mo1=greedyHaRegex.search("HaHaHaHaHa")
print(mo1.group())
nongreedyHaRegex=re.compile(r"(Ha){3,5}?")
mo2=nongreedyHaRegex.search("HaHaHaHaHaHa")
print(mo2.group())

phoneNumRegex=re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
phoneNumRegex.findall("cell: 123-456-7890 , work: 098-765-4321")


xmasRegex=re.compile(r"\d+\s\w+")
x=xmasRegex.findall("12 drummers, 11 pipers , 10 lords , 9 ladies , 8 maids 7 swans 6 geese 5 rings 4 birds , 3 hens")
print(x)


vowelRegex=re.compile(r"[aeiouAEIOU]")
x=vowelRegex.findall("RoboCop eats baby food. BABY FOOd.")
print(x)

consonantRegex=re.compile(r"[^aeiouAEIOU]")
x=consonantRegex.findall("RoboCop eats Baby Food. BABYFOOD!!!")
print(x)
#^ is start $ is end


atRegex=re.compile(r".at")
x=atRegex.findall("The cat in the hat sat on the flat mat eating rat.")
print(x)


# .* is anything





#  •	The ? matches zero or one of the preceding group.
#  •	The * matches zero or more of the preceding group.
#  •	The + matches one or more of the preceding group.
#  •	The {n} matches exactly n of the preceding group.
#  •	The {n,} matches n or more of the preceding group.
#  •	The {,m} matches 0 to m of the preceding group.
#  •	The {n,m} matches at least n and at most m of the preceding group.
#  •	{n,m}? or *? or +? performs a nongreedy match of the preceding group.
#  •	^spam means the string must begin with spam.
#  •	spam$ means the string must end with spam.
#  •	The . matches any character, except newline characters.
#  •	\d, \w, and \s match a digit, word, or space character, respectively.
#  •	\D, \W, and \S match anything except a digit, word, or space character, 
# respectively.
#  •	[abc] matches any character between the brackets (such as a, b, or c).
#  •	[^abc] matches any character that isn’t between the brackets.