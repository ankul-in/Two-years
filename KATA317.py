#kata
#https://www.codewars.com/kata/62ad72443809a4006998218a/train/python

Like = "Like"
Dislike = "Dislike"
Nothing = "Nothing"
def like_or_dislike(lst):
    counter=Nothing
    for i in lst:
        if i == Like:
            if counter==Like:
                counter=Nothing
            else:
                counter=Like
        elif i == Dislike:
            if counter==Dislike:
                counter=Nothing
            else:
                counter=Dislike
    return counter
        
print(like_or_dislike([Like, Like, Dislike, Like, Like, Like, Like, Dislike]))
