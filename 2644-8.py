import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
a,b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)
ans = [0] * (n+1)
ans[a] = 1
def dfs(v):
    visited[v] = 1
    
    for i in graph[v]:
        if visited[i] == 0:
            ans[i] = ans[v] + 1
            dfs(i)

dfs(a)
print(ans[b]-1)