import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(n,lst):
    if n == M:
        print(*lst)
        return
    
    prev = -1
    for j in range(n,N):
        if not v[j] and prev != num[j] and num[j] not in lst:
            v[j] = 1
            dfs(n+1,lst+[num[j]])
            v[j] = 0
            prev = num[j]



N,M = map(int,input().split())
num = list(map(int,input().split()))
v=[0]*(N)
num.sort()

if N == M:
    print(*num, end=' ')
    exit(0)

dfs(0,[])