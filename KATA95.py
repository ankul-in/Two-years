#kata
#https://www.codewars.com/kata/577e277c9fb2a5511c00001d/train/python
# def vowel_shift(text,n):
#     vowel=[]
#     for i in text:
#         if i in "aeiouAEIOU":
#             # text.replace(i,"*")
#             vowel.append(i)
#     for i in range(n):
#         vowel.append(vowel.pop(0))
#     for i,j in enumerate(text):
#         if j in "aeiouAEIOU":
#             text=text.replace(j,vowel[i])
# print(vowel_shift("This is a test!", 4))

def vowel_shift(text, n):
    vowels = [c for c in text if c in "aeiouAEIOU"]
    vowels = vowels[n % len(vowels):] + vowels[:n % len(vowels)]  

    result = []
    vowel_index = 0
    for c in text:
        if c in "aeiouAEIOU":
            result.append(vowels[vowel_index])
            vowel_index += 1
        else:
            result.append(c)
    return ''.join(result)

print(vowel_shift("This is a test!", 4))

