import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")


n, m, v = map(int,input().split())
grid = [[0] * (n+1) for _ in range(m)]
for _ in range(m):
    a, b = map(int,input().split())
    grid[a][b] = grid[b][a] = 1

bisit = [0] * (n+1)
disit = [0] * (n+1)

# print(grid)

def bfs(grid, v):
    bisit[v] = 1
    q = deque()
    q.append(v)

    while q:
        c_v = q.popleft()
        print(c_v, end= ' ')
        for i in range(n+1):
            if grid[c_v][i] == 1 and bisit[i] == 0:
                bisit[i] = 1
                q.append(i)

def dfs(grid, v):
    disit[v] = 1
    print(v, end= ' ')
    for i in range(n+1):
        if grid[v][i] == 1 and disit[i] == 0:
            dfs(grid,i)

bfs(grid,v)
print()
dfs(grid,v)

