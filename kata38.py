#kata finally can solve 8kyu katas in first go real achievemnt
def reverse_words(s):
    list=s.split()
    for i in list:
        rev=list[::-1]
        s=" ".join(rev)
        
    return s