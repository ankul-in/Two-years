#kata20
#sliding windows problem
#https://www.codewars.com/kata/671fd30696d3f42285f7d1f1/train/python
def window(length,offst,lst):
    result=[]
    for i in range(0, len(lst) - length + 1, offst):
        result.append(lst[i:i + length])


    return result


#for i in range(0,len(lst)-length+1,offset):
#result.append((lst[i:i+length]))