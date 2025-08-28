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


