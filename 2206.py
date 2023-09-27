import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n, m = map(int,input().split())
graph = [[list(map(int,input()))] for _ in range(n)]
visited = [[0]*m for _ in range(n)]


def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    dy = [1,-1,0,0]
    dx = [0,0,-1,1]
    chance = 0
    while q:
        cur_y, cur_x = q.popleft()
        cnt = 0
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            cnt += 1
            if 0<=next_y<n and 0<=next_x<m:
                if visited[next_y][next_x] == 0 and graph[next_y][next_x] == 0:
                    visited[next_y][next_x] = visited[cur_y][cur_x]+1
                    q.append((next_y,next_x))

                # 만약 더 이상 갈 수 있는 곳이 없다면 벽한번 부숴보기
                if not q and chance == 0 and cnt == 4:
                    visited[next_y][next_x] = visited[cur_y][cur_x]+1
                    q.append((next_y,next_x))
                    chance = 1

bfs()
print(visited[n-1][m-1])

