import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

def bfs(y,x):
    q= deque()
    q.append((y,x))
    visited[y][x] = 1
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    max_cnt = 1
    while q:
        cury, curx = q.popleft()
        
        for i in range(4):
            nexty = cury + dy[i]
            nextx = curx + dx[i]
            if(0<=nexty<n and 0<=nextx<m):
                if visited[nexty][nextx] == 0 and graph[nexty][nextx] == 1:
                    q.append((nexty,nextx))
                    visited[nexty][nextx] = 1
                    max_cnt+=1
    return max_cnt
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
ans=[]
cnt =0
maxtmp = 0
for j in range(n):
    for i in range(m):
        if visited[j][i] == 0 and graph[j][i] == 1:
            a = bfs(j,i)
            cnt+=1
            if maxtmp < a:
                maxtmp = a
if cnt == 0:
    maxtmp = 0
    
print(cnt)
print(maxtmp)