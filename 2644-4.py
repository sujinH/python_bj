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
cnt = 0
def dfs(v):
    global cnt
    visited[v] = 1
    for i in range(1,n+1):
       if graph[v][i] == 1 and visited[i] == 0:
          visited[i] = 1
          cnt += 1
          dfs(i)
       


for _ in range(m):
    x, y= map(int,input().split())
    graph[x][y] = graph[y][x] = 1

dfs(a)
# if len(result) == 0:
#   print(-1)
# else:
print(cnt)