#kata
#https://www.codewars.com/kata/59c3e819d751df54e9000098

def get_consective_items(items, key): 
    count=0
    countlist=[]
    key=str(key)
    for i in str(items):
        if i!=key:
            countlist.append(count)
            count=0
        else:
            count+=1
    countlist.append(count)
    return max(countlist)
print(get_consective_items('ascasdaiiiasdacasdiiiiicasdasdiiiiiiiiiiisdasdasdiii', 'i'))