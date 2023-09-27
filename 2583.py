import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

m, n, k = map(int,input().split())
graph = [[0]*n for _ in range(m)]
for _ in range(k):
    tmp = list(map(int,input().split()))

    for i in range(tmp[1],tmp[3]):
        for j in range(tmp[0],tmp[2]):
            graph[i][j] = 1

graph1 = graph[::-1]

q = deque()
cnt = 0
visited = [[0]*n for _ in range(m)]
def bfs(y,x,cnt):
    visited[y][x] = cnt
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    q.append((y,x))
    while q:
        cur_y, cur_x = q.popleft()
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if 0<=next_y<m and 0<=next_x<n:
                if graph1[next_y][next_x] == 0 and visited[next_y][next_x] == 0:
                    visited[next_y][next_x] = cnt
                    q.append((next_y,next_x))
cnt = 1
for i in range(m):
    for j in range(n):
        if graph1[i][j] == 0 and visited[i][j]==0:
            bfs(i,j,cnt)
            cnt += 1
many = max(map(max,visited))
print(many)
result = [0]*(m*n)
for i in range(m):
    for j in range(n):
        l = visited[i][j]
        if l != 0:
            result[l] += 1
result.sort()
for i in result:
    if i != 0:
        print(i, end=' ')