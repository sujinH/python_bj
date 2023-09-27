import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

def bfs(y,x):
    for j in range(n):
        for i in range(n):
            if graph[j][i] == '*' and visited[j][i] == 0:
                if y == j and i < x:
                    body['l_arm'] += 1
                    visited[j][i] = 1
                elif y == j and i > x:
                    body['r_arm'] += 1
                    visited[j][i] = 1
                elif y < j and i == x:
                    body['c'] += 1
                    visited[j][i] = 1
                elif y < j and i < x:
                    body['l_leg'] += 1
                    visited[j][i] = 1
                elif y < j and i > x:
                    body['r_leg'] += 1
                    visited[j][i] = 1


body = {'l_arm':0, 'r_arm':0, 'c':0, 'l_leg':0, 'r_leg':0}
n = int(input())
graph = [list(map(str,input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dy = [-1,1,0,0,-1,1,-1,1]
dx = [0,0,-1,1,-1,1,1,-1]
q = deque()
for j in range(n):
    for i in range(n):
        if graph[j][i] == '*':
            if graph[j-1][i] == '*' and graph[j][i-1] == '*' and graph[j+1][i] == '*' and graph[j][i+1] == '*':
                q.append((j,i))
                visited[j][i] = 1
                print(j+1,i+1)
                bfs(j,i)
                break

print(*body.values())