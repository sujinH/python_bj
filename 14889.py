import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(L,idx):
    global res
    if L == N//2:
        A=0
        B=0
        for i in range(N):
            for j in range(N):
                if v[i] and v[j]:
                    A+=s[i][j]
                elif not v[i] and not v[j]:
                    B+=s[i][j]

        res = min(res,abs(A-B))
        return
    

    for j in range(idx,N):
        if not v[j]:
            v[j] = 1
            dfs(L+1,idx+1)
            v[j] = 0

N = int(input())
s = [list(map(int,input().split())) for _ in range(N)]
v = [0 for _ in range(N)]
res = 2555000000
dfs(0,0)
print(res)