import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
# input = sys.stdin.readline()

def bfs(S,G):
    q = deque()
    q.append(S)
    visited[S] = 0

    while q:
        me =q.pop()

        if me == G:
            return visited[me]
        nextt =[me + U,me - D]
        for next in nextt:
            if 0<=next<F+1 and visited[next] == -1:
                visited[next] = visited[me] + 1 
                q.append(next)

    return "use the stairs"

# if flag == False:
#     print('use the stairs')

# 총 F층까지 있고, 내 위치는 S, 스타트링크위치 G, (UP, DOWN)
F, S, G, U, D = map(int,input().split())
visited = [-1]*(F+1)
cnt = 0

print(bfs(S,G))