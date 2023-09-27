import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(a,b,c):
    q = deque()
    q.append((a,b,c))
    visited[a][b][c] = 1

    while q:
        a,b,c = q.popleft()
        if a == n-1 and b == m-1: 
            return visited[a][b][c]

        for i in range(4):
            nexty = a + dy[i]
            nextx = b + dx[i]
            # graph가 갈 수 있는 길이고 아직 방문 하지 않았거나 graph가 1이고 c가 0이면
            if nextx < 0 or nextx >= m or nexty < 0 or nexty >= n:
                continue

            if graph[nexty][nextx] == '1' and c == 0:
                visited[nexty][nextx][1] = visited[a][b][c] + 1
                q.append((nexty,nextx,1))
            elif visited[nexty][nextx][c] == 0 and graph[nexty][nextx] == "0":
                visited[nexty][nextx][c] = visited[a][b][c] + 1
                q.append((nexty,nextx,c))
    return -1


n,m = map(int,input().split())
graph = [list((input().rstrip())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
print(bfs(0,0,0))