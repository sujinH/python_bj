import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(n):
    global cnt
    if len(lst)>0 and sum(lst) == S:
        cnt += 1

    for j in range(n,N):
        lst.append(num[j])
        dfs(j+1)
        lst.pop()

N,S = map(int,input().split())
num = list(map(int,input().split()))
lst = []
cnt = 0
dfs(0)
print(cnt)