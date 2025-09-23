#kata
#https://www.codewars.com/kata/5b6d065a1db5ce9b4c00003c/train/python
def dropzone(p, dropzones):
    distances={}
    for i in dropzones:
        x=(i[0]-p[0])**2+(i[1]-p[1])**2
        distances[x]=i
    return distances[min(distances)]


        
print(dropzone([6,8], [[3,2],[6,1],[7,9]]))


def dropzone(p, dropzones):
    return min(dropzones, key=lambda i: (i[0] - p[0])**2 + (i[1] - p[1])**2)