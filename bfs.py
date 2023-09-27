from collections import deque
visited = []
def bfs(graph,start_V):
    visited.append(start_V)
    q = deque(start_V)

    while q:
        cur = q.popleft()
        for v in graph[cur]:
            if v not in visited:
                visited.append(v)
                q.append(v)
    return visited

graph = {
    'A': ['B','D','E'],
    'B': ['A','C','D'],
    'C': ['B'],
    'D': ['A','B'],
    'E': ['A']

}
print(bfs(graph,'A'))