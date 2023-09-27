import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def bfs(student):
    for y in range(n):
        for x in range(n):
            
n=int(input())
graph = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]

for i in range(n*n):
    arr = list(map(int,input().split()))
    student = arr[0]
    a,b,c,d = arr[1],arr[2],arr[3],arr[4]

    bfs(student)