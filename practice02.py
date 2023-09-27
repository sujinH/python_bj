import sys
import math
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

N,M = map(int,input().split())
lst =[]

def dfs(start):
    if len(lst)==M:
        print(' '.join(map(str,lst)))
        return
    
    for i in range(start,N+1):
        if i not in lst:
            lst.append(i)
            dfs(i+1)
            lst.pop()
dfs(1)