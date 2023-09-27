import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

def bfs(j,i):
    visited = [[0]*m for _ in range(n)]
    q = deque([(j,i)])
    visited[j][i] = 1
    while q:
        cy, cx = q.popleft()
        if graph[cy][cx] == 2:
            return visited[cy][cx]

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < n and 0<= nx < m:
                if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[cy][cx] + 1
                    q.append((ny,nx))

    return -1

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
ans = [[0]*m for _ in range(n)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]
for j in range(n):
    for i in range(m):
        if graph[j][i] == 1:
            a = bfs(j,i)
            ans[j][i] = a
        elif graph[j][i] == 2:
            ans[j][i] == 0
        elif graph[j][i] == 0:
            ans[j][i] == 0
print(ans)