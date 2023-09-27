import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

# 입력 셋팅 (bfs구현)
n = int(sys.stdin.readline())
# graph 
graph = []
for i in range(n):
    s = list(map(int,sys.stdin.readline().rstrip()))
    graph.append(s)

# 방문
visited = [[0] * (n) for _ in range(n)]
counting = [0] * n*n
numOfHouses = 0
houseNum = 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(y,x):
    visited[y][x] = houseNum
    q = deque()
    q.append((y,x))
    count = 1
    while q:
        cur_y,cur_x = q.popleft()
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if 0<=next_x<n and 0<=next_y<n:
                if graph[next_y][next_x] == 1 and visited[next_y][next_x] == 0:
                    visited[next_y][next_x] = houseNum
                    q.append((next_y,next_x))
                    count += 1
            counting[houseNum] = count


for y in range(n):
    for x in range(n):
        if graph[y][x] == 1 and visited[y][x] == 0:
            bfs(y,x)
            houseNum += 1
            numOfHouses += 1
            
counting.sort()
print(numOfHouses)
for x in counting:
    if x != 0:
        print(x)

