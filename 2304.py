import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
graph = sorted(graph, key=lambda x: x[0])

paper = [0]*(graph[-1][0])

tmp = 0
for i in range(len(paper)):
    if i == graph[i][0]:
        paper[i] = graph[i][1]
        tmp = graph[i][1]
    else:
        paper[i] = tmp

print(paper)
