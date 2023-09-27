import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline
from collections import deque

# a = 최고층수 b = 현재 내 위치 c = 도달위치 d = up e = down

def bfs(start,goal):    
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        cur = q.popleft()
       
        if cur == goal:
            return visited[cur]

        for next in (cur + d, cur - e):
            if 0<next<=a and visited[next] == -1:
                q.append(next)
                visited[next] = visited[cur] + 1
    return "use the stairs"

a,b,c,d,e = map(int,input().split())
visited = [-1]*(a+1)

print(bfs(b,c))
print(visited)