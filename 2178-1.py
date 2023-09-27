import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n, m = map(int, input().split())
dx = [0,0,-1,1]
dy = [-1,1,0,0]

graph= [list(map(int,input())) for _ in range(n)]


def bfs(y,x):
    q = deque()
    q.append((y,x))

    while q:
        cur_y, cur_x = q.popleft()

        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if 0<=next_y<n and 0<=next_x<m:
                if graph[next_y][next_x] == 1:
                    graph[next_y][next_x] = graph[cur_y][cur_x] + 1
                    q.append((next_y,next_x))

bfs(0,0)
print(graph[n-1][m-1])

for i in range(n):
    for j in range(m):
        print(graph[i][j], end='')
    print()