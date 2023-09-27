import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
shape = [
    [(0, 0), (0, 1), (1, 0), (1, 1)], # ㅡ
    [(0, 0), (0, 1), (0, 2), (0, 3)], # ㅣ
    [(0, 0), (1, 0), (2, 0), (3, 0)], # ㅁ
    [(0, 0), (1, 0), (1, 1), (2, 1)], # h
    [(1, 0), (0, 1), (1, 1), (2, 0)], # h 회전
    [(1, 0), (1, 1), (0, 1), (0, 2)], # ...
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1)], # L
    [(0, 1), (1, 1), (2, 0), (2, 1)], # ...
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1)] # ㅓ

]   

def solution(y,x):
    global ans
    for j in range(19):
        tmp = 0
        for i in range(4):
            ny = y + shape[j][i][0]
            nx = x + shape[j][i][1]
            
            if 0<=ny<n and 0<=nx<m:
                tmp += graph[ny][nx]
        ans = max(ans,tmp)

ans = 0
for y in range(n):
    for x in range(m):
        solution(y,x)

print(ans)
