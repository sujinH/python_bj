import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n, m = map(int,input().split())
visited = [[0]*(m) for _ in range(n)]

graph = []
for _ in range(n):
    x = list(map(int,input().split()))
    graph.append(x)



def solution(graph):
    dx = [-1,0,1,-1,1,-1,0,1]
    dy = [-1,-1,-1,0,0,1,1,1]

    def bfs(y,x):
        q=deque()
        q.append((y,x))
        visited[y][x] = 0 
        cnt = 0
        while q:
            cur_y, cur_x = q.popleft()
            for i in range(8):
                next_y = cur_y +dy[i]
                next_x = cur_x +dx[i]
                if 0<=next_y<n and 0<=next_x<m:
                    if graph[next_y][next_x] == 1 and visited[next_y][next_x] == 0:
                        visited[next_y][next_x] =1
                        q.append((next_y,next_x))
                    else:
                        cnt += 1
            


    for y in range(n):
        for x in range(m):
            bfs(y,x)

solution(graph)
print(visited)