import sys
import math
sys.setrecursionlimit(10**6)
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(idx):
    if len(lst) == M:
        a = lst.copy()
        if a not in ans:
            ans.append(a)
        return
            
    for j in range(N):
        if tmp[j] not in lst:
            lst.append(tmp[j])
            dfs(j)
            lst.pop()
        elif tmp[j] in lst and tmp.count(tmp[j])>=2:
            lst.append(tmp[j])
            dfs(j)
            lst.pop()

N,M = map(int,input().split())
tmp = list(map(int,input().split()))
tmp.sort()
lst = []
ans = []
dfs(0)

for i in ans:
    print(*i)