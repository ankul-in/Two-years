#kata
#https://www.codewars.com/kata/587f1e1f39d444cee6000ad4/train/python

class Vector(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def add(self,another):
        if not isinstance(another,Vector):
            return ""
        return Vector(self.x+another.x,self.y+another.y)