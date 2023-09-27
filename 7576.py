import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

a, b = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(b)]
q = deque()
def bfs():

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    
    while q:
        cur_y, cur_x = q.popleft()

        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]

            if 0<= next_y < b and 0<= next_x < a:
                if arr[next_y][next_x] == 0:
                    arr[next_y][next_x] = arr[cur_y][cur_x] + 1
                    q.append((next_y,next_x))


cnt =0 
all = 0
tmp = 0
for i in range(b):
    for j in range(a):
        if arr[i][j] == 1:
            q.append((i,j))
            all += 1
        elif arr[i][j] == -1:
            tmp +=1
    if all == a*b - tmp:
        print(0)
        exit(0)
            
bfs()

for y in range(b):
    for x in range(a):
        if arr[y][x] == 0:
            print(-1)
            exit(0)
print(max(map(max,arr)) - 1)