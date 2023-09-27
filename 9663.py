import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def bfs(y,x,visited):
    q= deque()
    dy = [-1,1,0,0,-1,1,-1,1]
    dx = [0,0,-1,1,-1,1,1,-1]
    q.append((y,x))
    while q:
        curY, curX = q.popleft()

        for i in range(8):
            nY = curY + dy[i]
            nX = curX + dx[i]
            if 0<=nY<N and 0<=nX<N:
                if visited[nY][nX] != 0:
                    return -1
    return 0
                    



def check(lst,yy,xx):
    inf = []
    global cmt
    cnt_check = [0]*len(lst)
    for i in range(len(lst)):
        y = lst[i] // N
        x = lst[i] % N
        inf.append((y,x))
        # v[y][x] = 1
        
        yy[y] += 1
        xx[x] += 1
    cntY = 0
    cntX = 0
    for j in range(N):
        if yy[j] == 1:    
            cntY+=1
        if xx[j] == 1:    
            cntX+=1
    visited = [[0]*N for _ in range(N)]
    if cntX == N and cntY == N:
        for d in range(N):
            y1 = visited[d][0]
            x1 = visited[d][1]
            visited[y1][x1] = 1
            cc = bfs(y1,x1,visited)
            if cc != -1:
                cmt += 1
                return True
    return False
def dfs(n):
    global cnt
    yy = [0]*(N)
    xx = [0]*(N)
    if len(lst) == N:
        if check(lst,yy,xx):
            cnt+=1
        return
    pre = 0
    for j in range(n,place):
        if j not in lst :
            lst.append(j)
            dfs(j+1)
            lst.pop()

N = int(input())
place = N*N
lst=[]
cnt = 0
cmt = 0
v = [[0]*N for _ in range(N)]

dfs(0)
print(cnt)