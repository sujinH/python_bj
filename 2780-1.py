import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

t = int(input())

graph = {
    '0': [7],
    '1': [2,4],
    '2': [1,3,5],
    '3': [2,6],
    '4': [1,5,7],
    '5': [2,4,6,8],
    '6': [3,5,9],
    '7': [0,4,8],
    '8': [5,7,9],
    '9': [6,8]
}   

# visited = [0] * 10
def dfs(graph,start,n):
    # visited[start] = 1
    global cnt
    cnt += 1
    c -= 1

    while c >1:
        for x in graph[str(start)]:
            # if visited[i] == 0:
                dfs(graph,int(x),c)

# n = 2이면 최대 두 칸 이동
for _ in range(t):
    n = int(input())
    c = n
    # len(graph) = 10 0부터 ~1까지 돔
    cnt = 0
    for i in range(len(graph)):
        # if visited[i] == 0:
            dfs(graph, i, c)
    
    print(cnt)