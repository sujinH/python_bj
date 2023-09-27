import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

def bfs(y,x,cc):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    q = deque()
    q.append((y,x))
    graph[y][x] = 2
    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if graph[ny][nx] == 1 and graph[ny][nx] != 2:
                    graph[ny][nx] = 2
                    q.append((ny,nx))
                    cc += 1
    return cc



n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
cnt =0

ans = []
for j in  range(n):
    for i in  range(m):
        if graph[j][i] == 1:
            a = bfs(j,i,1)
            ans.append(a)
            cnt += 1

print(cnt)
if len(ans) == 0:
    print(0)
else:
    print(max(ans))