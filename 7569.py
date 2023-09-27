import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

m, n, h = map(int,input().split())

# graph 셋팅 과정, 한줄단위로 (리스트단위) 받으려고 노력함, for문을 줄이고 RunTimeError 방지.
# 실제 그래프
graph = [0]*h
for i in range(h):
    box1 = []
    for j in range(n):
        temp = list(map(int,input().split()))
        box1.append(temp)
    graph[i] = box1

# print(graph)

# 2차원 그래프
for i in range(n*h):
    for j in range(m):
        if 

def bfs(graph):
    q = deque()

    for 

bfs(graph)