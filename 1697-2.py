import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline
from collections import deque

def bfs(start,goal):
    q=deque()
    q.append(start)
    visited[start] = 0
    ans = []
    cnt = 0
    while q:
        cur = q.popleft()

        if cur == goal:
            ans.append(visited[cur])
            cnt += 1
            
        
        for next in (cur + 1, cur - 1, 2 * cur):
            if 0<=next<100001 and visited[next] == -1:
                q.append(next)
                visited[next] = visited[cur]+1
                
            elif 0<=next<100001 and next == goal and visited[next] != -1:
                cnt +=1
                

    return ans, cnt

n, k = map(int,input().split())
visited = [-1]*(100001)
ans1, cnt1 = bfs(n,k)

# for i in range(100001):
#     if visited[i] == ans1:
#         cnt += 1
print(ans1[0])
print(cnt1)
