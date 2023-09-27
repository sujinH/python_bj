import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(n,pr,lst):
    if len(lst) == M:
        ans.append(lst)
        return
    
    prev = 0
    for j in range(pr,N):
        if prev != num[j]:
            prev = num[j]
            dfs(n+1,j,lst+[num[j]])

N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
ans=[]
dfs(0,0,[])

for i in ans:
    print(*i)