#kata
#https://www.codewars.com/kata/5e16ffb7297fe00001114824/train/python


# def top3(products, amounts, prices):
#     price=[]
#     answer=[]
#     for i,j in zip(amounts,prices):
#         price.append(i*j)
#     newlist=zip(products,price)
#     sortedlist=sorted(newlist, key=lambda x: x[1],reverse=True)
#     for i,j in sortedlist:
#         answer.append(i)
#     return answer[:3]

def top3(products,amounts,prices):
    price=[i*j for i,j in zip(amounts,prices)]
    combined=list(zip(products,price))
    sortedList=sorted(combined, key=lambda x: x[1], reverse=True)
    return [product for product, value in sortedList[:3]]


#damn solutions
def top3(*args):
    return [item[0] for item in sorted(zip(*args), key=lambda x: x[1]*x[2], reverse=True)[:3]]

print(top3(['Computer', 'Cell Phones', 'Vacuum Cleaner'], 
            [3,          24,            8], 
            [199,        299,           399]))
    