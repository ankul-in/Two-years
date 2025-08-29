#logging
##import logging
# logging.basicConfig(level=logging.DEBUG,format="%(asctime)s-%(name)s-%(message)s",datefmt="%m/%d/%Y %H:%M:%S")
# logging.debug("this is debug")
# logging.info("this si info")
# logging.warning("this is warning")
# logging.error("this is error")
# # logging.critical("this is critical")
# logger=logging.getLogger(__name__)
# logger.propagate=False
# logger.info("hello from helper")
# logger=logging.getLogger(__name__)
# #create handler
# stream_h=logging.StreamHandler()
# file_h=logging.FileHandler("file.log")

# #level and format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter=logging.Formatter("%(name)s-%(levelname)s-%(message)s")
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)
# logger.warning("warning")
# logger.error("error")


# import traceback
# try:
#     a=[1,2,3]
#     val=a[4]
# except :#IndexError as e:
#     #logging.error(e,exc_info=True)
#     logging.error("the error is %s",traceback.format_exc())

# import time
# from logging.handlers import RotatingFileHandler , TimedRotatingFileHandler
# logger=logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# #handler=RotatingFileHandler("app.log",maxBytes=2000,backupCount=5)
# handler=TimedRotatingFileHandler("timed_test.log",when="s",interval=5,backupCount=5)
# logger.addHandler(handler)
# for i in range(1000):
#     logger.info("helloworld")


#json
##import json
# person={"name":"john","age":38,"city":"new york","hasChildren":False,"titles":["engineer","programmer"]}
# personJSON=json.dumps(person,indent=4,sort_keys=True)
# print(personJSON)
# # with open("person.json","w") as file:
# #     json.dump(person,file,indent=4)
# person=json.loads(personJSON)
# print(person)

# import json
# class User:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# # user=User("max",27)
# # def encode_user(o):
# #     if isinstance(o,User):
# #         return {"name":o.name,"age":o.age,o.__class__.__name__:True}
# #   else:
# #       raise TypeError("obj of type user is not recognizable")
# from json import JSONEncoder
# class userEncoder(JSONEncoder):
#     def default(self, o):
#         if isinstance(o,User):
#             return {"name":o.name,"age":o.age,o.__class__.__name__:True}
#         return JSONEncoder.default(self,o)
# #userJson=json.dumps(user,default=encodeuser)
# userJson=userEncoder().encode(user)
# def decode_user(dct):
#     if User.__name__ in dct:
#         return User(name=dct("name"),age=dct("age"))
#     return dct
# user=json.loads(userJson,object_hook=decode_user)
# print(type(user))
# print(userJson)




# import random

# a=random.random()
# print(a)
# a=random.uniform(1,10)
# print(a)
# a=random.randint(1,10)
# print(a)
# a=random.randrange(1,10)
# print(a)
# a=random.normalvariate(0,1)
# print(a)
# mylist=list("abcdefgh")
# print(mylist)
# a=random.choice(mylist)
# print(a)
# a=random.sample(mylist,3)
# print(a)
# a=random.choices(mylist,k=3)
# print(a)
# a=random.shuffle(mylist)
# print(mylist)

# random.seed(1)
# print(random.random())
# print(random.randint(1,10))

# random.seed(1)
# print(random.random())
# print(random.randint(1,10))

# random.seed(1)
# print(random.random())
# print(random.randint(1,10))

# import secrets
# a=secrets.randbelow(10)
# print(a)
# a=secrets.randbits(4)
# print(a)
# mylist=list("abcdefgh")
# a=secrets.choice(mylist)



# import numpy as np

# a=np.random.rand(3,4)
# print(a)
# a=np.random.randint(0,10,(3,4))
# print(a)
# arr=np.array([8, 9, 9, 5],[4 ,1 ,7 ,4],[1, 4, 5, 9])
# print(arr)
# np.random.shuffle(arr)
# print(arr)

# import functools
# # @mydecorator
# # def dosomething():
# #     pass
# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper():
#         print("start")
#         func()
#         print("end")
#     return wrapper
# @start_end_decorator
# # def print_name():
# #     print("alex")
# # print_name=start_end_decorator(print_name)
# # print_name()
# def add5(x):
#     return x+5
# print(help(add5))
# print(add5.__name__)


# import functools

# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(args,**kwargs):
#             for i in range(num_times):
#                 result=func(args,**kwargs)
#             return result
#         return wrapper
#     return decorator_repeat


# @repeat(num_times=3)
# def greet(name):
#     print(f"hello {name}")

# greet("alex")


