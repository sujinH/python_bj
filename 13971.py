import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def bfs(y,x):
    q = deque()
    q.append((y,x))
    visited = [[0]*m for _ in range(n)]
    visited[y][x] = 0
    dy =[-1,1,0,0]
    dx =[0,0,-1,1]
    cnt = 0
    while q:
        cy, cx = q.popleft()
        if graph[cy][cx] == 2 or graph[cy][cx] == 0:
            visited[cy][cx] = 0
            return visited[cy][cx]
     
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0<=ny<n and 0<=nx<m:
                if visited[ny][nx] == 0 and graph[ny][nx] == 1:
                    visited[ny][nx] = visited[cy][cx]+1
                    q.append((ny,nx))

                elif visited[ny][nx] == 0 and graph[ny][nx] == 2:
                    visited[ny][nx] = visited[cy][cx]+1
                    return visited[ny][nx]
        

n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
ans = [[0]*m for _ in range(n)]
for y in range(n):
    for x in range(m):
        v = bfs(y,x)
        ans[y][x] = v

for i in ans:
    print(*i)