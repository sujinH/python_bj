import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n,m,x,y,k = map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(n)]
coms = list(map(int,input().split()))
dice = [0,0,0,0,0,0]
dy = [0,0,1,-1]
dx = [1,-1,0,0]

for com in coms:
    ny = y + dy[com-1]
    nx = x + dx[com-1]

    if 0<= ny < n and 0<= nx < m:
        east, west, south, north, up, down = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]

        if com == 1:
            dice[4],dice[0],dice[5],dice[1] = west,up,east,down
        elif com == 2:
        elif com == 3:
        elif com == 4: