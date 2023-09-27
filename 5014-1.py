import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline
from collections import deque

def bfs(start,goal):
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        cur = q.popleft()


        if cur == c:
            return visited[cur]

        for next in (cur + d, cur - e):
            if 0<=next<a+1 and visited[next] == -1:
                visited[next] = visited[cur] + 1 
                q.append(next)

    return "use the stairs"

a,b,c,d,e = map(int,input().split())
visited = [-1] * (a+1)
print(bfs(b,c))