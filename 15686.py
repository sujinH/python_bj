import sys
from collections import deque

sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

# 가장 가까이에있는 치킨집의 좌표를 뱉음
def bfs(y,x):
    q = deque()
    q.append((y,x))
    # visited[y][x] = 1
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    global tmp
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<n and 0<=nx<n:
                if visited[ny][nx] == 0 and graph[ny][nx] == 2:
                    return ny, nx
                elif visited[ny][nx] == 0 and (graph[ny][nx] == 0 or graph[ny][nx] == 1):
                    visited[ny][nx] = 1
                    q.append((ny,nx))


n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
cnt = [[0]*n for _ in range(n)]
dist = 0
for y in range(n):
    for x in range(n):
        if graph[y][x] == 1:
            visited = [[0]*n for _ in range(n)]
            tmp = []
            visited[y][x] = 1 
            bfs_y, bfs_x = bfs(y,x)
            cnt[bfs_y][bfs_x] += 1
            # print(bfs_y,bfs_x)
            dist += (abs(bfs_y-y)+abs(bfs_x-x))

print(cnt)


