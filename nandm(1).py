import sys
import math
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(n,lst):
    if n==M:
        ans.append(lst)
        return
    for j in range(1,N+1):
        if v[j]==0:
            v[j]=1
            dfs(n+1,lst+[j])
            v[j]=0
    

N,M=map(int,input().split())
ans=[]
v=[0]*(N+1)
dfs(0,[])

for lst in ans:
    print(*lst)