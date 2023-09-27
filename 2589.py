import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def bfs(j,i):
    q = deque()
    q.append((j,i))
    visited = [[-1]*m for _ in range(n)]
    visited[j][i] = 0
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    while q:
        curY, curX = q.popleft()
       
        for i in range(4):
            nextY = curY + dy[i]
            nextX = curX + dx[i]
            if 0<=nextY<n and 0<=nextX<m:
                if visited[nextY][nextX] == -1: 
                    if graph[nextY][nextX] == 'L':
                        visited[nextY][nextX] = visited[curY][curX] + 1
                        q.append((nextY,nextX))
    return visited[curY][curX]

n,m = map(int,input().split())
graph = [list(map(str,input().strip())) for _ in range(n)]
# print(s)
ans = []
for j in range(n):
    for i in range(m):
        if graph[j][i] == 'L':
            res =bfs(j,i)
            ans.append(res)

print(max(ans))