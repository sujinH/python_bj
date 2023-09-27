import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n, m, v = map(int,input().split())

def bfs(v):
    q = deque()
    q.append(v)
    bfs_visited[v] = 1

    while q:
        popV = q.popleft()
        print(popV, end=' ')
        for i in range(1, n+1):
            if graph[popV][i] == 1 and bfs_visited[i] == 0:
                bfs_visited[i] = 1
                q.append(i)


bfs_visited = [0] * (n+1)
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

bfs(v)