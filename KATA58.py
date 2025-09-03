#kata
#https://www.codewars.com/kata/570597e258b58f6edc00230d/train/python


def array(string):
    x=string.split(",")
    if len(x)<3:
        return None
    else:
        x.pop(0)
        x.pop(-1)
        return " ".join(x)

print(array('1,2,3,4,5'))