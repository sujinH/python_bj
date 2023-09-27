import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())

visited = [0] * (n+1)
graph = [[0]*(n+1) for _ in range(n+1)]

m = int(input())
for i in range(m):
    a, b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    visited[v] = 1

    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)        

dfs(1)
cnt = 0
for i in visited:
    if i == 1:
        cnt += 1
print(cnt -1)