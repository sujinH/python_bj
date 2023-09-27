def dfs(graph,start_v):
    graph[start_v]

graph = {
    'A': ['B','D','E'],
    'B': ['A','C','D'],
    'C': ['B'],
    'D': ['A','B'],
    'E': ['A']

}
print(dfs(graph,'A'))