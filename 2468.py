import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(sys.stdin.readline())
grid = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
ma = max(map(max, grid))
mi = min(map(min, grid))
def safeArea(grid):
    col = len(grid[0])
    row = len(grid)
    visited = [[0]*col for _ in range(row)]

    def bfs(y,x,k):
        q = deque()
        q.append((y,x,k))
        dy= [-1,1,0,0]
        dx= [0,0,-1,1]
        visited[y][x] = 1
        while q:
            cy, cx, ck = q.popleft()
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if 0<=ny<row and 0<=nx<col:
                    if grid[ny][nx] > ck and visited[ny][nx] == 0:
                        visited[ny][nx] = 1
                        q.append((ny,nx,ck))


    result = [0]*(ma+1)
    for k in range(ma):
        cnt = 0
        visited = [[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] > k and visited[i][j] == 0:
                    bfs(i,j,k)
                    cnt += 1

        result[k] += cnt
    return max(result)

print(safeArea(grid))