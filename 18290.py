import sys
from itertools import combinations
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

def dfs(n):
    if len(lst) == K:
        print(*lst)
        break

    for j in range():
        lst.append(s[n][j])
        dfs(n+1)
        lst.pop()
lst=[]
N,M,K = map(int,input().split())
# a = list(map(int,input().split()))
s = [list(map(int,input().split())) for _ in range(N)]


dfs(0)
print(lst)