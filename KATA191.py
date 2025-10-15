#kata
#https://www.codewars.com/kata/584e93a70f60247eb8000132/train/python
# def perfect_square(square):
#     x=square.split("\n")
#     print(x)
#     y=[len(i) for i in x]
#     if all(i==y[0] for i in y): 
#         return True
#     return False

def perfect_square(square):
    rows = square.split("\n")
    size = len(rows)
    if all(row == "." * size for row in rows):
        return True
    return False


print(perfect_square('...\n...\n...'))
print(perfect_square('---\n---\n---'))