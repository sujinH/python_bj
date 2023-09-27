import sys
import copy
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

def bfs(y,x):
    q=deque([(y,x)])
    visited[y][x] = 1

    while q:
        cy,cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<n and 0<=nx<m and monitor[ny][nx] >= t and visited[ny][nx] == 0:
                q.append((ny,nx))
                visited[ny][nx] = 1



n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
monitor = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]
t = int(input())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

cnt = 0
tmp = 0
arr = []
for j in range(n):
    for i in range(m*3):
        if i%3 == 2:
            tmp += grid[j][i]
            arr.append(tmp//3)
            tmp=0
        else:
            tmp += grid[j][i]
arr2 = deque(arr)
for j in range(n):
    for i in range(m):
        monitor[j][i] = arr2.popleft()
for j in range(n):
    for i in range(m):
        if monitor[j][i] >= t and visited[j][i] == 0:
            bfs(j,i)
            cnt += 1

print(cnt)