import sys
from collections import deque
grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
col = len(grid[0])
row = len(grid)

visited = [[0]*col for _ in range(row)]

def numIsLands(grid):
    def bfs(y,x):
       q = deque()
       q.append((y,x))
       dy = [-1,1,0,0]
       dx = [0,0,-1,1]
       
       while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<row and 0<=nx<col:
                if grid[ny][nx] == '1' and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny,nx))

    cnt = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1' and visited[i][j] == 0: 
                bfs(i,j)
                cnt += 1
    return cnt

print(numIsLands(grid))