#kata
#https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python

def stock_list(stocklist, categories):
    answer=[]
    for j in categories:
        count=0
        for i in stocklist:
            code,quantity=i.split()
            if j==code[0]:
                count+=int(quantity)
        answer.append(f"({j} : {str(count)})")
                
    return " - ".join(answer)

print(stock_list(["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"],["A", "B", "C", "W"]))