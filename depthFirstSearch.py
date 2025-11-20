# #dfs #148

# # # Create an adjacency list for the graph
# from collections import defaultdict


# # def add_edge(adj, s, t):
# #     adj[s].append(t)
# #     adj[t].append(s)

# # # Recursive function for DFS traversal


# # def dfs_rec(adj, visited, s, res):
# #     # Mark the current vertex as visited
# #     visited[s] = True
# #     res.append(s)

# #     # Recursively visit all adjacent vertices that are not visited yet
# #     for i in adj[s]:
# #         if not visited[i]:
# #             dfs_rec(adj, visited, i, res)

# # # Main DFS function to perform DFS for the entire graph


# # def dfs(adj):
# #     visited = [False] * len(adj)
# #     res = []
# #     # Loop through all vertices to handle disconnected graph
# #     for i in range(len(adj)):
# #         if not visited[i]:
# #             # If vertex i has not been visited,
# #             # perform DFS from it
# #             dfs_rec(adj, visited, i, res)
# #     return res


# V = 6
# # Create an adjacency list for the graph
# adj = defaultdict(list)

# # Define the edges of the graph
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]

# # Populate the adjacency list with edges
# for e in edges:
#     add_edge(adj, e[0], e[1])
# res = dfs(adj)

# print(' '.join(map(str, res)))

###############################################################################################################
# from collections import defaultdict
# def add_edge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfs_rec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[i]:
#             dfs_rec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         if not visited[i]:
#             dfs_rec(adj,visited,i,res)
#     return res

# from collections import defaultdict
# def add_edge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
#     return res




# v=6
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     add_edge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))


##########################################################################################


# from collections import defaultdict
# class Graph:
#     def __init__(self):
#         self.graph=defaultdict(list)
#     def add_edge(self,u,v):
#         self.graph[u].append(v)
#     def dfs_iterative(self,start):
#         visited=set()
#         stack=[start]
#         while stack:
#             node=stack.pop()
#             if node not in visited:
#                 print(node,end=" ")
#                 visited.add(node)
#                 for neighbor in reversed(self.graph[node]):
#                     if neighbor not in visited:
#                         stack.append(neighbor)

# g=Graph()
# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(1,3)
# g.add_edge(1,4)
# g.add_edge(2,5)
# print("itrative DFS starting from vertex 0:")
# g.dfs_iterative(0)



# # i didint learn anything yet 


# from collections import defaultdict
# class Graph:
#     def __init__(self):
#         self.graph=defaultdict(list)
#     def add_edge(self,u,v):
#         self.graph[u].append(v)
#     def dfs_iterative(self,start):
#         visited=set()
#         stack=[start]
#         while stack:
#             node=stack.pop()
#             if node not in visited:
#                 print(node,end=" ")
#                 visited.add(node)
#                 for neighbor in reversed(self.graph[node]):
#                     if neighbor not in visited:
#                         stack.append(neighbor)

# g=Graph()
# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(1,3)
# g.add_edge(1,4)
# g.add_edge(2,5)
# print("itrative DFS starting from vertex 0:")
# g.dfs_iterative(0)


# from collections import defaultdict
# def add_edge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)

# def dfs_rec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[i]:
#             dfs_rec(adj,visited,i,res)

# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         if not visited[i]:
#             dfs_rec(adj,visited,i,res)
#          return res

# v=6
# adj=defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     add_edge(adj, e[0], e[1])
# res = dfs(adj)
# print("".join(map(str,res)))




# from collections import defaultdict
# def add_edge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfs_rec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[i]:
#             dfs_rec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         if not visited[i]:
#             dfs_rec(adj,visited,i,res)
#     return res

# v=6
# adj=defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     add_edge(adj, e[0], e[1])
# res = dfs(adj)
# print(" ".join(map(str,res)))


# from collections import defaultdict
# def add_edge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfs_rec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[i]:
#             dfs_rec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         if not visited[i]:
#             dfs_rec(adj,visited,i,res)
#     return res

# v=6
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     add_edge(adj,e[0],e[1])

# res=dfs(adj)
# print(" ".join(map(str,res)))

# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))
# #someday ima understand this 


#lets try today with my new wisdom tooth
# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))

# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))

# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))
    
# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[s]:
#             if not visited[i]:
#                 dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))


# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[s]:
#             if not visited[i]:
#                 dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# # print(" ".join(map(str,res)))



# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[s]:
#             if not visited[i]:
#                 dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))

# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[s]:
#             if not visited[i]:
#                 dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))



# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[s]:
#             if not visited[i]:
#                 dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))


# from collections import defaultdict

# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[s]:
#             if not visited[i]:
#                 dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))


# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[s]:
#             if not visited[i]:
#                 dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))


# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[s]:
#             if not visited[i]:
#                 dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))


# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[s]:
#             if not visited[i]:
#                 dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))



# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[s]:
#             if not visited[i]:
#                 dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))



# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))


# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))



# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))


# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))


# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRec(adj,visited,s,res):
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         if not visited[i]:
#             dfsRec(adj,visited,i,res)
# def dfs(adj):
#     visited=[False]*len(adj)
#     res=[]
#     for i in range(len(adj)):
#         dfsRec(adj,visited,i,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print(" ".join(map(str,res)))

# from collections import defaultdict

# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)

# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)

# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res

# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])

# res = dfs(adj)
# print( '-->'.join(map(str, res)))


# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))




# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))




# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))



# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))


# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))




# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))

# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))



# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))


# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))



# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))



# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))




# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))




# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))



# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))



# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))



# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))



# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))



# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))


# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))


# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))




# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))



# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))




# from collections import defaultdict
# def addEdge(adj, s, t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj, visited, s, res):
#     if visited[s]:
#         return
#     visited[s] = True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj, visited, i, res)
# def dfs(adj):
#     all_nodes = set(adj.keys())
#     for neighbors in adj.values():
#         all_nodes.update(neighbors)
#     visited = {node: False for node in all_nodes}
#     res = []
#     for node in all_nodes:
#         if not visited[node]:
#             dfsRes(adj, visited, node, res)
#     return res
# adj = defaultdict(list)
# edges = [[1, 2], [2, 0], [0, 3], [4, 5]]
# for e in edges:
#     addEdge(adj, e[0], e[1])
# res = dfs(adj)
# print( '-->'.join(map(str, res)))

# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))




# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))





# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))




# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))





# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))


# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))



# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))



# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))




# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))


# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))






# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))





# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))





# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))


# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))




# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))




# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))




# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))



# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))




# from collections import defaultdict
# def addEdge(adj,s,t):
#     adj[s].append(t)
#     adj[t].append(s)
# def dfsRes(adj,visited,s,res):
#     if visited[s]:
#         return
#     visited[s]=True
#     res.append(s)
#     for i in adj[s]:
#         dfsRes(adj,visited,i,res)
# def dfs(adj):
#     all_node=set(adj.keys())
#     for neighbors in adj.values():
#         all_node.update(neighbors)
#     visited={node:False for node in all_node}
#     res=[]
#     for node in all_node:
#         if not visited[node]:
#             dfsRes(adj,visited,node,res)
#     return res
# adj=defaultdict(list)
# edges=[[1,2],[2,0],[0,3],[4,5]]
# for e in edges:
#     addEdge(adj,e[0],e[1])
# res=dfs(adj)
# print("-->".join(map(str,res)))


from collections import defaultdict
def addEdge(adj,s,t):
    adj[s].append(t)
    adj[t].append(s)
def dfsRes(adj,visited,s,res):
    if visited[s]:
        return
    visited[s]=True
    res.append(s)
    for i in adj[s]:
        dfsRes(adj,visited,i,res)
def dfs(adj):
    all_node=set(adj.keys())
    for neighbors in adj.values():
        all_node.update(neighbors)
    visited={node:False for node in all_node}
    res=[]
    for node in all_node:
        if not visited[node]:
            dfsRes(adj,visited,node,res)
    return res
adj=defaultdict(list)
edges=[[1,2],[2,0],[0,3],[4,5]]
for e in edges:
    addEdge(adj,e[0],e[1])
res=dfs(adj)
print("-->".join(map(str,res)))