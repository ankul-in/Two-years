#kata
#https://www.codewars.com/kata/58e4377c46e371aee7001262/train/python
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

def triangle_area(triangle: Triangle) -> float:
    return abs(0.5*(triangle.a.x*(triangle.b.y-triangle.c.y)+triangle.b.x*(triangle.c.y-triangle.a.y)+triangle.c.x*(triangle.a.y-triangle.b.y)))

print(triangle_area(Triangle(Point(10, 10), Point(40, 10), Point(10, 50))))

#make it aesthetically pleasing man what is this above bs
def triangle_area(t):
    a,b,c = t.a,t.b,t.c
    return round(abs(a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y))/2,6)