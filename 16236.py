import sys
import copy
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

def bfs(y,x):
    q=deque([(y,x)])
    visited = [[0]*n for _ in range(n)]
    visited[y][x] = 1

    lv = 2;cnt = 0;time = 0
    while q:
        cy,cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<n and 0<=nx<n:
                if grid[ny][nx] < lv

n = int(input())
grid = [list(map(int,input().split())) for _ in range(n) ]
visited = [[0]*n for _ in range(n)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]

for j in range(n):
    for i in range(n):
        if grid[j][i] == 9:
            grid[j][i] = 0
            bfs(j,i)
            break