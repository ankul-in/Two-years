#file handling in python
f=open("hello.txt","r")
print(f)
file=open("hello.txt","r")
file.close()
f=open("hello.txt","r")
print("Filename:",f.name)
print("Mode:",f.mode)
print("is closed? ",f.closed)
f.close()
print("is closed? ",f.closed)

file=open("hello.txt","r")
content=file.read()
print(content)
file.close()
with open("hello.txt","r") as file:
    content =file.read()
    print(content)


try:
    file=open("hello.txt","r")
    content=file.read()
    print(content)
finally:
    file.close