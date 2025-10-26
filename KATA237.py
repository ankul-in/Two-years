#kata
#https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python

def find_needle(haystack):
    for i,j in enumerate(haystack):
        if j=="needle":
            return f"found the needle at position {i}"
        
def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'