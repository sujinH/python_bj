import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(n,lst):
    if n == M:
       ans.append(lst)
       return
    
    prev = 0
    for j in range(N):
        if v[j] == 0 and prev != tmp[j]:
            prev=tmp[j]
            v[j] = 1
            dfs(n+1,lst+[tmp[j]])
            v[j] = 0



N,M = map(int,input().split())
tmp = list(map(int,input().split()))
tmp.sort()
ans=[]
v = [0]*(N+1)
dfs(0,[])
for lst in ans:
    print(*lst)