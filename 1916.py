import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")


def dfs(n):
    if len(lst)>0 and n == N:
        ans.append(sum(lst))

    for j in range(n+1,N+1):
        lst.append(graph[n][j])
        dfs(j)
        lst.pop()

N = int(input())
M = int(input())
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b,cost = map(int,input().split())
    graph[a][b] = graph[b][a] = cost


a1,b1 = map(int,input().split())
lst = []
ans = []
dfs(a1)
print(min(ans))