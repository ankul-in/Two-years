# #python intermediate course https://youtu.be/HGOBQPFzWKo
# #dictionary key value pair
# # mydict={"name":"max","age":38,"city":"newYork"}
# # print(mydict)
# # value =mydict["age"]
# # print(value)
# # mydict["email"]="max@xyz.com"
# # mydict["email"]="cool@max.py"
# # del mydict["name"]
# # mydict.pop("age")
# # mydict.popitem["city"]
# # print(mydict)
# # try:
# #     print(mydict["lastname"])
# # except:
# #     print("error")
# # for key,value in mydict.items():
# #     print(key)
# # mydict_cpy=mydict
# # print(mydict_cpy)
# # mydict_cpy["email"]="max@xyz.com"
# # print(mydict_cpy)
# # print(mydict)
# # mydict.update(mydict_cpy)
# # # mydict={"name":"max","age":38,"city":"newYork"}
# # my_dict={3:9,6:36,9:81}
# # print(my_dict)
# # value=my_dict[3]
# # print(value)
# # mytuple=(8.7)
# # my_dict={mytuple:15}
# # print(my_dict)
# # #set
# # myset={1,2,3}
# # #print(myset)
# # # print(myset)
# # # myset=set{"hello","hello"}
# # # # yourset=set{(1,,3,45,6)}
# # # print(yourset)
# # myset.add(1)
# # myset.discard(1)
# # print(myset)
# # for x in myset:
# #     print(x)
# #     if x==1:
# # #         print("1")
# # odds={1,3,5,7,9,11}
# # evens={2,4,6,8,10}
# # primes={2,3,5,7}
# # u=odds.union(evens)
# # print(u)
# # i=odds.intersection(primes)
# # print(i)
# # a=evens.intersection(primes)
# # print(a)
# setA={1,2,3,4,5,6,7,8,9}
# setB={1,2,3,10,11,12}
# setC={7,8}
# # print(setB.difference(setA))
# # print(setA.difference(setB))
# # setA.update(setB)
# # print(setA)
# # setA.intersection_update(setB)
# # print(setA.difference_update(setB))
# # print(setA.symmetric_difference_update(setB))
# # print(setA.issubset(setB))
# # print(setB.issubset(setA))
# # print(setA.issuperset(setB))
# # print(setA.isdisjoint(setB))
# # print(setA.isdisjoint(setC))
# # setB=setA
# # print(setB)
# # setB.add(7)
# # setB=setA.copy()
# # print(setB)
# # a=frozenset([1,2,3,4])
# # a.add(2)
# # a.remove(1)
# # print(a)
# #strings
# # my_string="Hello World"
# # print(my_string)
# # my_string="""
# # multiline
# # # comment"""
# # my_string="helloworld"
# # char=my_string[0].upper()
# # print(char)
# # substring=my_string[1:6:2]
# # print(substring)
# # name="tom"
# # sentence= my_string+name
# #print(sentence)
# # for i in greeting:
# #       print(i)
# # if "e" in greeting:
# #        print("yes")
# #else:
# #   print("no")
# myString="  HelloWorld  "
# # #print(myString.strip())
# # print(myString.upper())
# # # print(myString.lower())
# # print(myString.startswith("H"))
# # print(myString.endswith("world"))
# # #print(myString.find("W"))
# # # print(myString.count("o"))
# # # print(myString.replace("World","universe"))
# myString="how are you doing"
# myList=myString.split("o")
# # # print(myList)
# # newString="".join(myList)
# # print(newString)
# myList=["a"]*6
# # print(myList)
# # myString=""
# # for i in myList:
# #     myString+=i
# #     print(myString)
# myString="  ".join(myList) #good
# print(myString)

# from timeit import default_timer as timer
# # start=timer()
# var = "Tom"
# my_string="the variable is %s"%var
# # print(my_string)
# int=5
# var=5
# var2=8
# mystring="the decimal is {:.2f} and {}".format(var,var2)
# print(mystring)
# mystring=f"the variable is {var*2}and {var2}"

# #collections
# from collections import Counter
# a="aaaaabbbbbccccccc"
# mycount=Counter(a)
# print(mycount.keys())
# print(mycount.values())
# print(mycount.most_common(3)[0][0])
# # print(list(mycount.elements()))
# from collections import namedtuple
# point=namedtuple("point","x,y")
# pt=point(1,-4)
# # print(pt)
# from collections import OrderedDict
# OrderedDict=OrderedDict()
# OrderedDict["a"]=1
# OrderedDict["s"]=1
# OrderedDict["b"]=1
# OrderedDict["c"]=1

# OrderedDict["a"]=1
# # print(OrderedDict)
# from collections import defaultdict
# d=defaultdict(list)
# d["a"]=1
# d["b"]=2
# # print(d["b"])
# from collections import deque
# d=deque()
# d.append(1)
# d.append(2)
# print(d)
# d.appendleft(3)
# print(d)
# d.pop()
# print(d)
# print(d.popleft())
# d.extend([4,5,6])
# d.extendleft([4,5,6])
# print(d)
# d.rotate(1)
# d.rotate(2)
# print(d)


#itertools


# from itertools import product
# a=[1,2]
# b=[3]
# prod=product(a,b,repeat=2)
# # print(list(prod))
# from itertools import permutations
# a=[1,2,3]
# per=permutations(a,2)
# # print(list(per))
# from itertools import combinations,combinations_with_replacement    
# a=[1,2,3,4]
# comp=combinations(a,2)
# print(list(comp))
# combWR=combinations_with_replacement(a,2)
# print(list(combWR))
# from itertools import accumulate
# import operator
# a=[1,5,2,3,4]
# # acc=accumulate(a,func=operator.mul)
# # print(a)
# # print(list(acc))
# acc=accumulate(a,func=max)
# # print(list(acc))
# from itertools import groupby
# def smallerThan3(x):
#     return x<3
# a=[1,2,3,4]
# group_obj=groupby(a,key=smallerThan3)
# print(group_obj)
# for key,value in group_obj:
#     print(key,list(value))

#groupby dictionaries by age

# from itertools import count , cycle,repeat
# # for i in count(10):
# #     print(i)

# a=[1,2,3]
# for i in cycle(a):
#     print(i)

# #lambda arguments:experession
# add0=lambda x:x+10
# # print(add0(5))
# mult=lambda x,y:x*y
# print(mult(2,7))

# listPoint=[[1,2],[15,1],[5,-1],[10,4]]
# listPointSorted=sorted(listPoint,key=lambda x:x[0]+x[1])
# print(listPoint)
# # print(listPointSorted)
# a=[1,2,3,4,5]
# b=map(lambda x:x*2,a)
# print(list(b))

# c=[x*2 for x in a]
# print(c)
#filter(func,seq)
# a=[1,2,3,4,5]
# b=filter(lambda x:x%2==0,a)
# print(list(b))
# c=[x for x in a if x%2==0]
# # print(c)
# from functools import reduce
# a=[1,2,3,4,5,6]
# product_a=reduce(lambda x,y:x*y,a)
# print(product_a)

#exception

# try:
# except ZeroDivisionError as e:
# else:
# finally:
class ValueTooHighError(Exception):
    pass
def test_value(x):
    if x>100:
        raise ValueTooHighError("value is too high")
test_value(200)