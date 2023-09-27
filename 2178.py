import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

# n, m = map(int,input().split())

# graph = [list(map(int,input())) for _ in range(n)]
# dy = [-1,1,0,0]
# dx = [0,0,-1,1]

# def bfs(y,x):
#     q = deque()
#     q.append((y,x))

#     while q:
#         cur_y, cur_x = q.popleft()
#         for i in range(4):
#             next_y = cur_y + dy[i]
#             next_x = cur_x + dx[i]

#             if 1<=next_x<m and 1<=next_y<n:
#                 if graph[next_y][next_x] == 1:
#                     graph[next_y][next_x] = graph[cur_y][cur_x] + 1
#                     q.append((next_y,next_x))

# bfs(0,0)
# print(graph[n-1][m-1])