# #bfs algorithm #154
# #still didnt learn dfs yet but anyways 
# def bfs(adj):
#     V=len(adj)
#     res=[]
#     s=0
#     from collections import deque
#     q=deque()
#     visited=[False]*V
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# if __name__=="__main__":
#     adj = [[1,2], [0,2,3], [0,4], [1,4], [2,3]]
#     ans=bfs(adj)
#     for i in ans:
#         print(i, end=" ")



#BFS of the Disconnected Graph
# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res

# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         if not visited[i]:
#             bfsOfGraph(adj,i,visited,res)
#     return res

# if __name__=="__main__":
#     adj = [[1,2], [0,2,3], [0,4], [1,4], [2,3]]
#     ans=bfsDisconnected(adj)
#     for i in ans:
#         print(i,end=" ")
# #todo tommorow grind both bfs and dfs 

# from collections import deque
# def bfsofGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res

# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         if not visited[i]:
#             bfsofGraph(adj,i,visited,res)
#     return res

# if __name__=="__main__":
#     adj=[[1,2],[0,2,3],[0,4],[1,4],[2,3]]
#     ans=bfsDisconnected(adj)
#     for i in ans:
#         print(i,end=" ")


# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         if not visited[i]:
#             bfsOfGraph(adj,i,visited,res)
#     return res
# if __name__=="__main__":
#     adj=[[1,2],[0,2,3],[0,4],[1,4],[2,3]]
#     ans=bfsDisconnected(adj)
#     for i in ans:
#         print(i,end=" ")

#         #still nothing feel nothing cant remember tthis
# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)

#     return res

# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         if not visited[i]:
#             bfsOfGraph(adj,i,visited,res)
#     return res

# if __name__=="__main__":
#     adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
#     ans=bfsDisconnected(adj)
#     for i in ans:
#         print(i,end=" ")

# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         if not visited[i]:
#             bfsOfGraph(adj,i,visited,res)
#     return res
# if __name__=="__main__":
#     adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
#     ans=bfsDisconnected(adj)
#     for i in ans:
#         print(i,end=" ")

# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         if not visited[i]:
#             bfsOfGraph(adj,i,visited,res)
#     return res
# if __name__=="__main__":
#     adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
#     ans=bfsDisconnected(adj)
#     for i in ans:
#         print(i,end=" ")


# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         if not visited[i]:
#             bfsOfGraph(adj,i,visited,res)
#     return res
# if __name__=="__main__":
#     adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
#     ans=bfsDisconnected(adj)
#     for i in ans:
#         print(i,end=" ")

# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         if not visited[i]:
#             bfsOfGraph(adj,i,visited,res)
#     return res
# if __name__=="__main__":
#     adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
#     ans=bfsDisconnected(adj)
#     for i in ans:
#         print(i,end=" ")

# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         if not visited[i]:
#             bfsOfGraph(adj,i,visited,res)
#     return res
# if __name__=="__main__":
#     adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
#     ans=bfsDisconnected(adj)
#     for i in ans:
#         print(i,end=" ")



# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         if not visited[i]:
#             bfsOfGraph(adj,i,visited,res)
#     return res
# if __name__=="__main__":
#     adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
#     ans=bfsDisconnected(adj)
#     for i in ans:
#         print(i,end=" ")



# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# if __name__=="__main__":
#     adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
#     ans=bfsDisconnected(adj)
#     for i in ans:
#         print(i,end=" ")
 

# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# if __name__=="__main__":
#     adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
#     ans=bfsDisconnected(adj)
#     for i in ans:
#         print(i,end=" ")



# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# if __name__=="__main__":
#     adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
#     ans=bfsDisconnected(adj)
#     for i in ans:
#         print(i,end=" ")

# from collections import deque

# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
# #     print(i,end=" ")


# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end=" ")


# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end=' ')



# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end=" ")



# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end=" ")


# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end=" ")

# from collections import deque

# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end=" ")

# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:

#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[5,1],[7,1],[3,1],[6,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end=" ")

# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end=" ")


#idk what am i doing with these 4 algorithms but smth might need these 4
# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end="-->")


# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end="-->")



# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end="-->")




# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end="-->")





# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end="-->")

# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end="-->")

# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end="-->")



# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end="-->")


# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end="-->")

# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end="-->")


# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end="-->")


# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end="-->")


# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end="-->")


# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end="-->")




# from collections import deque
# def bfsOfGraph(adj,s,visited,res):
#     q=deque()
#     visited[s]=True
#     q.append(s)
#     while q:
#         curr=q.popleft()
#         res.append(curr)
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x]=True
#                 q.append(x)
#     return res
# def bfsDisconnected(adj):
#     V=len(adj)
#     res=[]
#     visited=[False]*V
#     for i in range(V):
#         bfsOfGraph(adj,i,visited,res)
#     return res
# adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
# ans=bfsDisconnected(adj)
# for i in ans:
#     print(i,end="-->")


from collections import deque
def bfsOfGraph(adj,s,visited,res):
    q=deque()
    visited[s]=True
    q.append(s)
    while q:
        curr=q.popleft()
        res.append(curr)
        for x in adj[curr]:
            if not visited[x]:
                visited[x]=True
                q.append(x)
    return res
def bfsDisconnected(adj):
    V=len(adj)
    res=[]
    visited=[False]*V
    for i in range(V):
        bfsOfGraph(adj,i,visited,res)
    return res
adj=[[7,3],[6,2],[4,1],[3,1],[],[],[],[]]
ans=bfsDisconnected(adj)
for i in ans:
    print(i,end="-->")