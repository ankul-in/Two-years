#opposite neighbours cancel each other out 

# def dir_reduc(arr):
#     dir=[]
#     n=0
#     e=0
#     for i in arr:
#         if i=="NORTH":
#             n+=1
#         elif i=="SOUTH":
#             n-=1
#         elif i=="EAST":
#             e+=1
#         elif i=="WEST":
#             e-=1
#     if n>0:
#         for i in range(n):
#             dir.append("NORTH")
#     else:
#         for i in range(abs(n)):
#             dir.append("SOUTH")
#     if e>0:
#         for i in range(e):
#             dir.append("EAST")
#     else:
#         for i in range(abs(e)):
#             dir.append("WEST")
        

#     return dir
# import string
# def dir_reduc(arr):
#     dir=arr[:]
#     dir="".join(dir)
#     for i in range(100):
#         if "NORTHSOUTH" in dir:
#             dir.replace("NORTHSOUTH","")
#         if "SOUTHNORTH" in dir:
#             dir.replace("SOUTHNORTH","")
#         if "EASTWEST" in dir:
#             dir.replace("EASTWEST","")
#         if "WESTEAST" in dir:
#             dir.replace("WESTEAST","")
#     return dir
# def dir_reduc(arr):
#     dir=arr[:]
#     for i in range(len(arr)):
#         if dir[i]=="NORTH" and dir[i+1]=="SOUTH" :
#             dir.pop(i)
#             dir.pop(i+1)
#         if dir[i]=="SOUTH" and dir[i+1]=="NORTH" :
#             dir.pop(i)
#             dir.pop(i+1)
#         if dir[i]=="EAST" and dir[i+1]=="WEST" :
#             dir.pop(i)
#             dir.pop(i+1)
#         if dir[i]=="WEST" and dir[i+1]=="EAST" :
#             dir.pop(i)
#             dir.pop(i+1)
#     return dir
def dir_reduc(arr):
    
    
    opposite={}
    opposite={
    "EAST":"WEST",
    "NORTH":"SOUTH",
    "WEST":"EAST",
    "SOUTH":"NORTH"
}
    dir=[]
    for i in arr:
        if dir and opposite[i] == dir[-1]:
            dir.pop()
        else:
            dir.append(i)
    return dir