import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline
from collections import deque

def bfs(y,x,color):
    q = deque()
    q.append((y,x,color))
    visited[y][x] = 1
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    while q:
        cy, cx, cc = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<n and 0<=nx<n:
                if visited[ny][nx] == 0 and graph[ny][nx] == color:
                    visited[ny][nx] = 1
                    q.append((ny,nx,cc))

def bfs2(y,x,color1):
    q = deque()
    q.append((y,x,color1))
    visited_2[y][x] = 1
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    while q:
        cy, cx, cc1 = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<n and 0<=nx<n:
                if visited_2[ny][nx] == 0:
                    if cc1 == 'x' and (graph[ny][nx] == "R" or graph[ny][nx] == "G"):
                        visited_2[ny][nx] = 1
                        q.append((ny,nx,'x'))
                    
                    elif cc1 == "B" and graph[ny][nx] == "B":
                        visited_2[ny][nx] = 1
                        q.append((ny,nx,cc1))


n = int(input())
graph = [list(input().strip()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
visited_2 = [[0]*n for _ in range(n)]
# print(s)
r_cnt = 0
g_cnt = 0
b_cnt = 0
rg_cnt2 = 0
b_cnt2 = 0
for  y in range(n):
    for  x in range(n):
        if visited[y][x] == 0:
            if graph[y][x] == "R":
                bfs(y,x,"R")
                r_cnt += 1
            elif graph[y][x] == "G":
                bfs(y,x,"G")
                g_cnt += 1
            elif graph[y][x] == "B":
                bfs(y,x,"B")
                b_cnt += 1

        if visited_2[y][x] == 0:
            if graph[y][x] == "R" or graph[y][x] == "G":
                bfs2(y,x,"x")
                rg_cnt2 += 1
            elif graph[y][x] == "B":
                bfs2(y,x,"B")
                b_cnt2 += 1
print(r_cnt+g_cnt+b_cnt,rg_cnt2+b_cnt2)