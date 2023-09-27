import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(n):
    if n== N:
        print(lst)
        return

    for j in range(N):
        lst.append(graph[n][j])
        dfs(n+1)
        lst.pop()
prev = -1
N = int(input())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
lst=[]

dfs(0)