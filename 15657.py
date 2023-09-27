import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(n):
    if len(lst) == M:
        print(*lst)
        return
    
    for j in range(n,N+1):
        if j not in lst:
            lst.append(j)
            dfs(j+1)
            lst.pop()

N,M = map(int,input().split())
lst=[]
dfs(1)