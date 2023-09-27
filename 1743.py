import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def bfs(y,x):
    cnt = 0
    dy = [1,-1,0,0]
    dx = [0,0,-1,1]
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    cnt = 1
    while q:
        c_y, c_x = q.popleft()

        for i in range(4):
            n_y = c_y + dy[i]
            n_x = c_x + dx[i]
            if 0<=n_y<n and 0<=n_x<m:
                if visited[n_y][n_x] == 0 and graph[n_y][n_x] != 0:
                    visited[n_y][n_x] = 1
                    q.append((n_y,n_x))
                    cnt += 1
    return cnt

# 입력 처리 
n,m,k = map(int,input().split())
graph = [[0]*m for _ in range(n)]
for _ in range(k):
    r,c = map(int,input().split())
    graph[r-1][c-1] = 1

ans = []
# bfs 돌리기
visited = [[0]*m for _ in range(n)]
for j in range(n):
    for i in range(m):
        if graph[j][i] == 1 and visited[j][i] == 0:
            v = bfs(j,i)
            ans.append(v)
print(max(ans))