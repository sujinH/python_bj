import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n,m,x,y,k = map(int,input().split())
maap = [list(map(int,input().split())) for _ in range(n)]
comands = list(map(int,input().split()))
# 동서북남
dy = [0,0,1,-1]
dx = [1,-1,0,0]
dice = [0,0,0,0,0,0]
# up, down, front, back, left,right
def turn(dir,y,x):
    global dice
    # 동쪽
    if dir == 1:
        dice = [dice[3],dice[0],dice[2],dice[5],dice[4],dice[1]]
    # 서쪽
    elif dir == 2:
        dice = [dice[2],dice[4],dice[3],dice[0],dice[5],dice[1]]
    # 북쪽
    elif dir == 3:
        dice = [dice[4],dice[2],dice[1],dice[3],dice[5],dice[0]]
    # 남쪽
    elif dir == 4:
        dice = [dice[1],dice[2],dice[4],dice[3],dice[0],dice[5]]

    if maap[y][x] ==0:
        maap[y][x] = dice[0]

    else:
        dice[0] = maap[y][x]
        maap[y][x] = 0

for cmd in comands:
    ny = y + dy[cmd-1]
    nx = x + dx[cmd-1]

    if 0<=ny<n and 0<=nx<m:
        turn(cmd,ny,nx)
        print(dice[0])
        y,x = ny,nx
