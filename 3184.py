import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline
from collections import deque

# dfs구현
def bfs(y,x):
    q = deque()
    q.append((y,x))
    visited[y][x] = 1

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    oo = 1
    vv = 0
    while q:
        cur_y, cur_x = q.popleft()

        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]

            if 0<=next_y<r and 0<=next_x<c:
                if visited[next_y][next_x] == 0 and graph[next_y][next_x] != '#':
                    q.append((next_y,next_x))
                    visited[next_y][next_x] = 1

                    if graph[next_y][next_x] == 'o':
                        oo += 1
                    elif graph[next_y][next_x] == 'v':
                        vv += 1
    return oo, vv


# . 빈공간 # 울타리 o 양 v 늑대
# 영역안의 양의 수 > 늑대 수 양이 이김 늑대 쫓아냄 
# 늑대 수가 더 많다면 양을 모조리 먹음
r, c = map(int,input().split())
graph = [list(input().strip()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]

o_cnt1 = 0 ; v_cnt1 = 0

for j in range(r):
    for i in range(c):
        if graph[j][i] == 'o':
            o_cnt1 += 1
        elif graph[j][i] == 'v':
            v_cnt1 += 1

if o_cnt1 == 0 or v_cnt1 == 0:
    print(o_cnt1, v_cnt1)
    exit(0)


o_cnt = 0 ; v_cnt = 0
for j in range(r):
    for i in range(c):
        if visited[j][i] == 0 and graph[j][i] == 'o':
            oo, vv = bfs(j,i)
            if oo > vv:
                v_cnt1 -= vv
            else:
                o_cnt1 -= oo

print(o_cnt1, v_cnt1)