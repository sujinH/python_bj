import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")


n = int(input())
a, b = map(int,input().split())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0
result = []
def bfs(start):
    q = deque()
    q.append(start)
    global cnt
    visited[start] = 1
    while q:
        if b in q:
            result.append(cnt)
        cur = q.popleft()
        cnt += 1
        for i in range(1, n+1):
            if graph[cur][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1 

for _ in range(m):
    x, y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1
bfs(a)
if len(result) == 0:
    print(-1)
else:
    print(result[0])


