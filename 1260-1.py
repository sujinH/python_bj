import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(v):
    dfs_visi[v] = 1
    print(v, end = ' ')
    for i in range(1, n+1):
        if dfs_visi[i] == 0 and graph[v][i] == 1:
            dfs_visi[i] = 1
            dfs(i)
def bfs(v):
    q = deque()
    q.append(v)
    bfs_visi[v] = 1
    while q:
        popV = q.popleft()
        print(popV, end = ' ')
        for i in range(1, n+1):
            if graph[popV][i] == 1 and bfs_visi[i] == 0:
                bfs_visi[i] = 1
                q.append(i)


n, m, v = map(int, input().split())
dfs_visi = [0] * (n+1)
bfs_visi = [0] * (n+1)
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


dfs(v)
print()
bfs(v)