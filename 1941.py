import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def bfs(si,sj):
    q=deque()
    vv = [[0]*5 for _ in range(5)]

    q.append((si,sj))
    vv[si][sj]=1
    cnt = 1
    di = [1,-1,0,0]
    dj = [0,0,-1,1]

    while q:
        ci,cj = q.popleft()
        for i in range(4):
            ni = ci + di[i]
            nj = cj + dj[i]
            if 0 <=ni<5 and 0<=nj<5 and vv[ni][nj]==0 and v[ni][nj]==1:
                q.append((ni,nj))
                vv[ni][nj]=1
                cnt+=1

    return cnt==7

def check():
    for i in range(5):
        for j in range(5):
            if v[i][j] == 1:
                return bfs(i,j)

def dfs(n,cnt,scnt):
    global ans
    if n==25:
        if cnt == 7 and scnt>=4:
            if check():
                ans+=1

        return
    
    v[n//5][n%5] = 1 # 학생번호를 이용해서 방문기록
    dfs(n+1,cnt+1, scnt+int(arr[n//5][n%5]=='S'))
    v[n//5][n%5] = 0 
    dfs(n+1,cnt,scnt)

arr = [input() for _ in range(5)]
v = [[0]*5 for _ in range(5)] 
ans= 0
# 학생번호(0~24), 포함학생수, 다솜파학생수 
dfs(0,0,0)
print(ans)