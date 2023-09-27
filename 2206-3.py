import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def bfs(a,b,c):
    q = deque()
    q.append((a,b,c))
    visited[a][b][c] = 1

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    while q:
        y,x,c = q.popleft()
        if y == n-1 and x == m-1:
            return visited[y][x][c]
        
        for i in range(4):
            nextY = y + dy[i]
            nextX = x + dx[i]

            if 0>nextY or nextY>=n or 0>nextX or nextX >= m:
                continue

            # 갈수있는데 방문하지 않은 경우
            if visited[nextY][nextX][c] == 0 and graph[nextY][nextX] == 0:
                q.append((nextY,nextX,c))
                visited[nextY][nextX][c] = visited[y][x][c] + 1
            elif graph[nextY][nextX] == 1 and c == 0:
                q.append((nextY,nextX,1))
                visited[nextY][nextX][1] = visited[y][x][0] + 1
    return -1

n, m = map(int, input().split())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

print(bfs(0,0,0))