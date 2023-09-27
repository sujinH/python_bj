import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(now,destIdx):
    global cnt
    if now == dest[destIdx]:
        if destIdx == m-1:
            cnt += 1
            return
        else:
            destIdx += 1
    y,x = now
    visited[y][x] = 1

    for i in range(4):
        ny,nx = y+dy[i], x+dx[i]
        if 0<=ny<n and 0<=nx<n and grid[ny][nx] == 0 and visited[ny][nx] == 0:
            dfs([ny,nx],destIdx)
    visited[y][x] = 0
    return
    

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]
dest = []
cnt = 0
for _ in range(m):
    y,x = map(int,input().split())
    dest.append([y-1,x-1])

dfs(dest[0],1)

print(cnt)