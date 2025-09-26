#kata
#https://www.codewars.com/kata/5fc4349ddb878a0017838d0f/train/python


def red_knight(N, P):
    start=N
    counter=0
    while N<P:
        N+=2
        P+=1
        counter+=1
    if counter % 2 == 0:
        return ("White",P+start)
    else:
        return ("Black",P+start)
print(red_knight(1, 5))
#now i realised the problem was multiplication not simulation
def red_knight(N, P):
    if (N+P) % 2 == 0:
        return ("White",2*P)
    else:
        return ("Black",2*P)



#top answer
def red_knight(N, P):
    return ('White' if P % 2 == N else 'Black', P * 2)



