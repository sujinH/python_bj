import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

def dfs(n,idx):
    global res
    if n == N:
        res.append(sum(lst))
        # print(lst)
        return
    
    for j in range(3):
        if j != idx:
            lst.append(s[n][j])
            dfs(n+1,j)
            lst.pop()


N=int(input())
s = [list(map(int,input().split())) for _ in range(N)]
lst=  []
res = []
dfs(0,-1)
print(min(res))
# print(res)