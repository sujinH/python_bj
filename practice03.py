import sys
import math
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

N,M = map(int,input().split())
lst = []

def dfs(n):
    if len(lst)==M:
        print(*lst)
        return
    
    for j in range(1,N+1):
        if j not in lst:
            lst.append(j)
            dfs(n+1)
            lst.pop()


dfs(0)