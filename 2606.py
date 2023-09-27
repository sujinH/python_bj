import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(v):
    visited[v] = 1
    global cnt
    for i in range(1,n+1):
        if visited[i] == 0 and graph[v][i]:
            visited[i] = 1
            # print(i)
            cnt += 1
            dfs(i)

n = int(input())
network = int(input())
visited = [0] * (n+1)
graph = [[0] * (n+1) for _ in range(n+1)]
cnt = 0
for i in range(network):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(1)
print(cnt)