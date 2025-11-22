#kata
#https://www.codewars.com/kata/5b728f801db5cec7320000c7/train/python

def solve(s,k): 
    chars = list(s)
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if k == 0:
            break
        i = 0
        while i < len(chars) and k > 0:
            if chars[i] == letter:
                chars.pop(i)   
                k -= 1
            else:
                i += 1
    
    return ''.join(chars)
