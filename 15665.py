import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(n,idx,lst):
    if n == M:
        print(*lst)
        return
    
    prev = -1
    for j in range(idx,N):
        if prev != num[j] and prev<num[j]:
            print(prev, num[j])
            dfs(n+1,idx,lst+[num[j]])
            prev = num[j]



N,M = map(int,input().split())
num = list(map(int,input().split()))
v=[0]*(N)
num.sort()

if N == M:
    print(*num, end=' ')
    exit(0)

dfs(0,0,[])