import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
# 보드크기 n, 사과 개수 k
n=int(input())
k=int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    y,x = map(int,input().split())
    graph[y][x] = 2

info ={}
l = int(input())
for _ in range(l):
    y,x = map(str,input().split())
    info[int(y)]=x
dy=[0,1,0,-1]
dx=[1,0,-1,0]
y,x=1,1
graph[y][x]=1
d=0
time = 0
q=deque([(1,1)])
while True:
    ny,nx = y+dy[d],x+dx[d] 

    if ny<=0 or ny > n or nx<=0 or nx > n or (ny,nx) in q:
        break

    if graph[ny][nx] != 2:
        a,b = q.popleft()
        graph[a][b] = 0

    y,x = ny,nx
    graph[y][x] =1
    q.append((ny,nx))
    time += 1

    if time in info.keys():
        if info[time] == 'L':
            d=(d+3)%4
        elif info[time] == 'D':
            d=(d+1)%4

print(time+1)
