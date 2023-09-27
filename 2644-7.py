import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
a, b = map(int,input().split())

m = int(input())
visited = [0] * (n+1)
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1

result= [0] * (n+1)
cnt = 0
def dfs(v):
    global cnt
    
    visited[v] = 1
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] == 0:
            cnt+=1
            if v == b: 
             result.append(cnt)
            dfs(i)   
        

dfs(a)

print(cnt)
# cnt = 0
# def bfs(a,b):
#     visited[a] = 1
#     q = deque()
#     q.append(a)
#     global cnt
#     while q:
#         cur = q.popleft()
#         if b == cur:
#             break
#         for i in range(1, n+1):
#             if graph[cur][i] == 1 and visited[i] == 0:
#                 visited[i] = 1
#                 q.append(i)
#         cnt += 1
            

# bfs(a,b)
