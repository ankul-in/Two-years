#kata
#https://www.codewars.com/kata/59cd0535328801336e000649/train/python


#from decimal import Decimal, getcontext

# def interest(p, r, n):
#     getcontext().prec = 30  
#     p = Decimal(p)
#     r = Decimal(r)
#     simpAmount = p + (p * r * n)
#     A = p
#     for _ in range(n):
#         A += A * r
#     return [round(simpAmount), round(A)]


def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return round(principal+simple_interest)
def calculate_compound_interest(principal, rate, time, n=1):
    compound_interest = principal * (1 + rate / (100 * n))**(n * time) - principal
    return round(principal+compound_interest)

def interest(p, r, n):
    r=100*r
    return [calculate_simple_interest(p,r,n),calculate_compound_interest(p,r,n)]

#why cant i think like this
def interest(principal, interest, periods):
    return [round(principal * (1 + interest * periods)),
            round(principal * (1 + interest) ** periods)]