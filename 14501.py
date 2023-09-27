import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(n):
    if n > M+1:
        print(lst)
        return
    
    for j in range(n,M+1):
        lst.append(day[j][1])
        dfs(day[j][0]+n)
        lst.pop()

M = int(input())
day = [0]*(M+1)
v = [0]*(M+1)
lst =[]
for i in range(1,M+1):
    t,p = map(int,input().split())
    day[i] = (t,p)


dfs(1)
