import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
a,b = map(int,input().split())
if a>=b:
    a,b = b,a
m = int(input())
visited = [0] * (n+1) 
graph = [[0]*(n+1) for _ in range(n+1)]
cnt = 0
result =[]
def dfs(a):
    global cnt
    if a == b:
        result.append(cnt)
    cnt+=1
    visited[a] = 1
    for i in range(1,n+1):
        if graph[a][i] == 1 and visited[i] == 0:
            dfs(i)

for _ in range(m):
    y, x = map(int,input().split())
    graph[y][x] = graph[x][y] = 1

dfs(a)
if len(result)>0:
    print(result[0])
elif len(result) == 0:
    print(-1)    