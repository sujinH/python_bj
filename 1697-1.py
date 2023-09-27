import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")


import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

m, n, h = map(int,sys.stdin.readline().split())

# graph 셋팅 과정, 한줄단위로 (리스트단위) 받으려고 노력함, for문을 줄이고 RunTimeError 방지.
# 실제 그래프
graph = []
for i in range(n*h):
        temp = list(map(int, sys.stdin.readline().split()))
        graph.append(temp)

# print(graph)

# print("graph: {}".format(graph))
# print("graph2: {}".format(graph2))

result = graph.copy()
def bfs(graph):
    q = deque()
    dy = [-1,1,0,0,n,-n]
    dx = [0,0,-1,1,0,0]
    for y in range(n*h):
        for x in range(m):
            if graph[y][x] == 1:
                q.append((y,x))

    while q:
        cur_y , cur_x = q.popleft()

        for i in range(6):
            n_y = cur_y + dy[i]
            n_x = cur_x + dx[i]

            if (n_y % n == 0 and (n_y - cur_y == 1)) or (cur_y % n == 0 and (cur_y - n_y == 1)):
                continue
            else:
                if 0<= n_y < n*h and 0<=n_x<m:
                    if graph[n_y][n_x] == 0:
                        graph[n_y][n_x] = 1
                        result[n_y][n_x] = 1
                        q.append((n_y, n_x))
                        result[n_y][n_x] = result[cur_y][cur_x] + 1
            
         
bfs(graph)
ans =0
for i in result:
    for x in i:
        if x == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))
           
print(ans-1)
# print(result)