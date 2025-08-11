#a graph problem
from collections import deque
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []
#print("the graph include-->",graph)
#mango seller is one whos name ends with y
def mangoSeller(name):
    return name[-1]=="y"

def searchPeople(people):
    searchQueue=deque()
    searchQueue += graph['you']
    searched=[]
    while searchQueue:
        
        
        person=searchQueue.popleft()
        if not person in searched:
            if mangoSeller(person):
                print("mango Seller is-->",person)
                return True
            else:
                searchQueue+=graph[person]
                searched.append(person)
    return False
    
searchPeople("you")


    
