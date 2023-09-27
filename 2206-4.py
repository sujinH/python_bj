import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline
from collections import deque

def bfs(y,x,c):
    while q:
        y,x,c = q.popleft()
        if y == n-1 and x == m-1:
            return visited[y][x][c]
        
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if visited[ny][nx][c] == 0 and graph[ny][nx] == 0:
                    q.append((ny,nx,c))
                    visited[ny][nx][c] = visited[y][x][c] + 1
                elif graph[ny][nx] == 1 and c==0:
                    q.append((ny,nx,1))
                    visited[ny][nx][1] = visited[y][x][c] + 1
    return -1

n,m = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]
visited=[[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
q = deque([(0,0,0)])
dy = [-1,1,0,0]
dx = [0,0,-1,1]
print(bfs(0,0,0))

