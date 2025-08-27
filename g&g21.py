#https://www.geeksforgeeks.org/problems/lucky-numbers2911/1&selectedLang=python3

def isLucky(n):
    counter=2
    pos=n
    while counter <=pos:
        if pos%counter ==0:
            return 0
        pos -= pos//counter
        counter += 1

    return 1
print(isLucky(3))