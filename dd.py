import sys
import math
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

# dfs구현
def dfs(n):
    if len(lst) == M:
        print(*lst)
        return
    
    for j in range(n,N):
        if num[j] not in lst:
            lst.append(num[j])
            dfs(j+1)
            lst.pop()

N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
lst=[]

dfs(0)