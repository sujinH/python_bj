import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")


# def bfs(p1,p2):
#     visited[p1] = 1
#     visited[p2] = 1
#     q = deque()
#     q.append(p1)
#     global cnt

#     while q:
#         popV = q.popleft()
#         cnt += 1
#         for i in range(1, n+1):
#             if graph[popV][i] == 1 and visited[i] == 0:
#                 q.append(i)
#                 visited[i] = 1
#             else:
#                 cnt -= 1
def dfs(start):
    visited[start] =1
    global cnt
    cnt+=1

    if start == b:
        result.append(cnt)

    for i in range(1, n+1):
        if graph[start][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)
            
   



# 사람이 1~n명이 있음
n = int(input())

# 서로 다른 두 사람
a, b = map(int, input().split())
# 루프 몇 번 도는지
m = int(input())
cnt = 0
# visited 와 graph 셋팅
visited = [0] * (n+1)
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x, y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1
result = []
dfs(a)
# bfs(7, 8)
print(result)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)