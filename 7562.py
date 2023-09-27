import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline
from collections import deque

# bfs 구현
def bfs(y,x):
    q= deque()
    q.append((y,x))
    visited[y][x] = 1

    dy = [-2,-1,2,1,-2,-1,1,2]
    dx = [-1,-2,-1,-2,1,2,2,1]

    while q:
        cur_y, cur_x = q.popleft()

        if cur_y == y2 and cur_x == x2:
            return visited[cur_y][cur_x]


        for i in range(8):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]

            if 0<=next_y<I and 0<=next_x<I:
                if visited[next_y][next_x] == 0:
                    visited[next_y][next_x] = visited[cur_y][cur_x] + 1
                    q.append((next_y,next_x))


t = int(input())

for _ in range(t):
    # 체스판 한 변의 길이
    I = int(input())
    # 나이트가 현재 있는 칸
    y1, x1 = map(int,input().split())
    # 나이트가 이동하려고 하는 칸
    y2, x2 = map(int,input().split())

    visited = [[0]*I for _ in range(I)]
    cnt = bfs(y1,x1)
    print(cnt-1)