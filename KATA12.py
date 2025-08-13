# rgb to hex


def rgb(r, g, b):
    arr=[]
    arr.append(r)
    arr.append(g)
    arr.append(b)
    y=""
    for i in arr:
        if i >= 0 and i<=255:
            x=hex(i)[2:].zfill(2)
            y=y+x.upper()
        else:
            if i<0:
                x="00"
                y=y+x
            elif i>255:
                x="FF"
                y=y+x
    return y


# def rgb(r,g,b):
#     round= lambda x: min(255,max(x,0))
#     return {(":02X"*3).format(round(r),round(g),round(b))}