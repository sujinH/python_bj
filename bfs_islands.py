from collections import deque
def numIsLands(grid):
    col = len(grid[0]) 
    row = len(grid)
    numOfIslands = 0
    visited = [[False]*col for _ in range(row)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    def bfs(y,x):
        q = deque()
        q.append((y,x))
        visited[y][x] = True
        while q:
            cur_y, cur_x = q.popleft()
            for i in range(4):
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]

                if 0<=next_x<col and 0<=next_y<row:
                    if visited[next_y][next_x] == False and grid[next_y][next_x] == "1":
                        visited[next_y][next_x] = True
                        q.append((next_y,next_x))

    for y in range(row):
        for x in range(col):
            if 0<=x<col and 0<=y<row:
                if visited[y][x] == False and grid[y][x] == "1":
                    bfs(y,x)
                    numOfIslands += 1
    print(numOfIslands)            

print(numIsLands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]))
