#kata
#https://www.codewars.com/kata/52a723508a4d96c6c90005ba/train/python

# def sing(): 
#     arr=[]
#     for i in range(1000):
#         n=99-i
#         if n==1:
#             arr.append(f"{n} bottle of beer on the wall, {n} bottle of beer.")
#             arr.append(f"Take one down and pass it around, {n-1} bottles of beer on the wall.")
#             continue
#         arr.append(f"{n} bottles of beer on the wall, {n} bottles of beer.")
#         arr.append(f"Take one down and pass it around, {n-1} bottles of beer on the wall.")
#         if n==-1:
#             arr.append("No more bottles of beer on the wall, no more bottles of beer.")
#             arr.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
#             n=99
#     return arr


def sing():
    arr = []
    for n in range(99, -1, -1):
        if n > 1:
            arr.append(f"{n} bottles of beer on the wall, {n} bottles of beer.")
            arr.append(f"Take one down and pass it around, {n-1} bottle{'s' if n-1 != 1 else ''} of beer on the wall.")
        elif n == 1:
            arr.append("1 bottle of beer on the wall, 1 bottle of beer.")
            arr.append("Take one down and pass it around, no more bottles of beer on the wall.")
        else:
            arr.append("No more bottles of beer on the wall, no more bottles of beer.")
            arr.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
    return arr


print(sing()[25])