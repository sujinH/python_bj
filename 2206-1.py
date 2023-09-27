import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")


def bfs(y,x,chance):
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    dy = [1,-1,0,0]
    dx = [0,0,-1,1]

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if visited[ny][nx] == 0 and graph[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny,nx))
        
        if not q and chance == 0:
            

    return graph[n-1][m-1]

n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

# bfs(0,0)
print(bfs(0,0,0))
print(visited)