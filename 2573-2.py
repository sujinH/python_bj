import sys
from collections import deque
import copy
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(j,i):
    q = deque([(j,i)])
    visited[j][i] = 1

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]    
            nx = cx + dx[i]    
            if 0<= ny <n and 0<= nx <m:
                if graph[ny][nx] != 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny,nx))
                elif graph[ny][nx] == 0:
                    cnt[cy][cx] += 1

    return 1
while(True):
    visited = [[0]*m for _ in range(n)]
    cnt = [[0]*m for _ in range(n)]
    result = []
    #  빙산 그래프를 싹 돌면서 얼마나 녹았는지 cnt그래프에 개수 기록
    for j in range(n):
        for i in range(m):
            if graph[j][i] != 0 and visited[j][i] == 0:
                result.append(bfs(j,i))

    # 빙산그래프에서 이전에 녹았던 애들을 빼줘서 다음 빙산그림을 위해 빙산 세팅
    for j in range(n):
        for i in range(m):
            graph[j][i] -= cnt[j][i]
            if graph[j][i] < 0:
                graph[j][i] = 0
                
    
    if len(result) == 0:
        break
    elif len(result) >= 2:
        check = True
        break

if check:
    print(len(result)-1)
else:
    print(0)

