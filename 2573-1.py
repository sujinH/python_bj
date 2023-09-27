import sys
from collections import deque
import copy
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

check = False
day=0

def bfs(j,i):
    q = deque()
    q.append((j,i))
    visited[j][i] = 1
    while q:
        cury, curx = q.popleft()

        for i in range(4):
            nexty = cury + dy[i]
            nextx = curx + dx[i]
            if 0<= nexty <n and 0<= nextx < m:
                if graph[nexty][nextx] != 0 and visited[nexty][nextx] == 0:
                    visited[nexty][nextx] = 1
                    q.append((nexty,nextx))
                elif graph[nexty][nextx] == 0:
                    cnt[cury][curx] += 1

    return 1

while True:
    visited = [[False]*m for _ in range(n)]
    cnt = [[0]*m for _ in range(n)]
    result=[]
    for j in range(n):
        for i in range(m):
            if graph[j][i] != 0 and visited[j][i] == 0:
                result.append(bfs(j,i))

    for j in range(n):
        for i in range(m):
            graph[j][i] -= cnt[j][i]
            if graph[j][i] < 0:
                graph[j][i] = 0

    if len(result) ==0:
        break
    if len(result) >= 2:
        check = True
        break
    day += 1

if check:
    print(day)
else:
    print(0)