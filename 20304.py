import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def bfs(k):
    q = deque()
    q.append(k)
    visited[k] = 1


    while q:
        q.popleft()
        [s[k-1]]

n,k = map(int,input().split())
s = [i for i in range(1,n+1)]
visited = [0]*(n+1)
bfs(k)
