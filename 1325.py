import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline
def bfs(i):
    q = deque()
    q.append(i)
    visited[i]=1
    cnt = 1
    while q:
        ci = q.popleft()
        
        for j in graph[ci]:
            if visited[j] == 0:
                visited[j] = 1
                q.append(j)
                cnt += 1
    return cnt
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

ans = [0]*(n+1)
for i in range(1,n+1):
    visited = [0]*(n+1)
    cn = bfs(i)
    ans[i]=(cn)

pre_max = max(ans)
res = []

for x in range(n+1):
    if ans[x] == pre_max:
        print(x, end=' ')