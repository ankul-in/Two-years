# 14 to check if string is anagram or not
a=input("enter first string-->")
b=input("enter second string-->")
length=len(a)
count=0
if len(a)==len(b):
    for i in a:
        for j in b:
            if i==j:
                count=count+1
    if count==length:
        print("string are anagram")
else:
    print("string are not anagram")


