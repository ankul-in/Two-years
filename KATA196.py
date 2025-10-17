#kata
#https://www.codewars.com/kata/55b75fcf67e558d3750000a3/train/python

class Block:
    def __init__(self,arr):
        self.width=arr[0]
        self.height=arr[2]
        self.length=arr[1]
    def get_width(self):
        return self.width
    def get_length(self):
        return self.length
    def get_height(self):
        return self.height
    def get_surface_area(self):
        return 2*(self.width*self.length+self.width*self.height+self.length*self.height)
    def get_volume(self):
        return self.width*self.length*self.height
    
#what am i doing
class Block(object):
    def __init__(self, wlh):
        self.w, self.l, self.h = w,l,h = wlh
        self.v = w*h*l
        self.a = 2 * (w*l + w*h + l*h)
    
    def get_width(self):        return self.w
    def get_length(self):       return self.l
    def get_height(self):       return self.h
    def get_volume(self):       return self.v
    def get_surface_area(self): return self.a