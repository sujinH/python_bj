import sys
import math
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")


def dfs(n):
    global cnt
    if sum(lst) == S and len(lst)>0:
        cnt += 1

    for j in range(n,N):
        lst.append(tmp[j])
        dfs(j+1)
        lst.pop()

N,S = map(int,input().split())
tmp= list(map(int,input().split()))
lst = []
cnt = 0
dfs(0)
print(cnt)