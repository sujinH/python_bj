import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

r,c = map(int,input().split())
graph = [list(map(str,input().strip())) for _ in range(r)]
q_ji = deque()
q_fire = deque()
visi_ji = [[0]*c for _ in range(r)]
visi_fire = [[0]*c for _ in range(r)]

def bfs():
    dy = [-1,1,0,0]
    dx = [-0,0,-1,1]
    
    while q_fire:
        cur_y, cur_x = q_fire.popleft()
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]

            if 0<= next_y < r and 0<= next_x < c:
                if visi_fire[next_y][next_x] == 0 and graph[next_y][next_x] != '#':
                    visi_fire[next_y][next_x] = visi_fire[cur_y][cur_x] + 1
                    q_fire.append((next_y,next_x))
    
    while q_ji:
        cur_y, cur_x = q_ji.popleft()
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]

            if 0<= next_y < r and 0<= next_x < c:
                if visi_ji[next_y][next_x] == 0 and graph[next_y][next_x] != '#':
                    if visi_fire[next_y][next_x] == 0 or visi_fire[next_y][next_x] > visi_ji[cur_y][cur_x] + 1:
                        visi_ji[next_y][next_x] = visi_ji[cur_y][cur_x] + 1
                        q_ji.append((next_y,next_x))
            else:
                return visi_ji[cur_y][cur_x]
    return "IMPOSSIBLE"

for j in range(r):
    for i in range(c):
        if graph[j][i] == 'J':
            q_ji.append((j,i))
            visi_ji[j][i] = 1
        elif graph[j][i] == 'F':
            q_fire.append((j,i))
            visi_fire[j][i] = 1

print(bfs())
