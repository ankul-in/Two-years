#kata
#https://www.codewars.com/kata/52de9bd621c71b919c000592/train/python


def in_sphere(coords, radius):
    sum=0
    for x in coords:
        sum=sum+x**2
    radiusArea=radius**2
    return sum<=radiusArea