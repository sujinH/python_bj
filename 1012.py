import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

t = int(input())

def bfs(y,x):
        q = deque()
        q.append((y,x))
        dy = [1,-1,0,0]
        dx = [0,0,-1,1]
        visited[y][x] = 1

        while q:
            cur_y,cur_x = q.popleft()

            for i in range(4):
                n_y = cur_y + dy[i]
                n_x = cur_x + dx[i]
                if 0<= n_y < n and 0<= n_x <m:
                    if graph[n_y][n_x] == 1 and visited[n_y][n_x] == 0:
                        q.append((n_y,n_x))
                        visited[n_y][n_x] = 1
# graph 전처리 하기
for _ in range(t):
    m, n, k = map(int,input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1

    cnt = 0
    for p in range(n):
        for q in range(m):
            if graph[p][q] == 1 and visited[p][q] == 0:
                bfs(p,q)
                cnt += 1

    
    print(cnt)