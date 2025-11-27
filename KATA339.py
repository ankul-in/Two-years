#Kata
#https://www.codewars.com/kata/562f91ff6a8b77dfe900006e/train/python

import math
def movie(card, ticket, perc):
    systemA = 0
    systemB = card
    n = 0
    while True:
        n += 1
        systemA += ticket
        systemB += ticket * (perc ** n)
        if systemA > math.ceil(systemB):
            return n
print(movie(500, 15, 0.9))  



# def systemA(n,ticket):
#     return n*ticket
# def systemB(n,card,ticket,perc):
#     sum=card
#     ticketPrice=ticket
#     for i in range(n):
#         sum+=perc*ticketPrice
#         ticketPrice=perc*ticketPrice
#     return sum

# def movie(card, ticket, perc):
#     i=0
#     while True:
#         print(i)
#         i+=1
#         if systemA(i,ticket)>systemB(i,card,ticket,perc):
#             return i
        


# print(movie(500, 15, 0.9))