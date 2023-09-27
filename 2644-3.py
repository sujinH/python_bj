import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
# 입력값 받는 부분
n = int(input())
a, b = map(int,input().split())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0] * (n+1)
result = []
def dfs(v, num):
    num += 1
    visited[v] = True

    if v == b:
        result.append(num)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)

for _ in range(m):
    x, y= map(int,input().split())
    graph[x][y] = graph[y][x] = 1

dfs(a, 0)

if len(result) == 0:
  print(-1)
else:
  print(result[0]-1)