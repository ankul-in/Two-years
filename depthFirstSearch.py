#dfs
from collections import defaultdict

def add_edge(adj,s,t):
    adj[s].append(t)
    adj[t].append(s)

def dfs_rec(adj,visited,s,res):
    visited[s]=True
    res.append(s)

    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj,visited,i,res)
        
def dfs(adj):
    visited=[False]*len(adj)
    res=[]

    for i in range(len(adj)):
        if not visited[i]:
            dfs_rec(adj,visited,i,res)
    return res



v=6
adj=defaultdict(list)
edges=[[1,2],[2,0],[0,3],[4,5]]
for e in edges:
    add_edge(adj,e[0],e[1])
res=dfs(adj)
print(" ".join(map(str,res)))