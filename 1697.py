import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(x, y, d):
    global cnt

    if graph[x][y] == 0:
        graph[x][y] = 2
        cnt += 1

    for _ in range(4):
        next_d = (d + 3) % 4
        next_x = x + dx[next_d]
        next_y = y + dy[next_d]

        if graph[next_x][next_y] == 0:
            dfs(next_x, next_y, next_d)
            return
        d = next_d

    next_d = (d + 2) % 4
    next_x = x + dx[next_d]
    next_y = y + dy[next_d]

    if graph[next_x][next_y] == 1:
        return
    
    dfs(next_x, next_y, next_d)


n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# d => 0,3,2,1 순서로 돌아야함. 북/서/남/동
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
cnt = 0
dfs(r, c, d)
print(cnt)