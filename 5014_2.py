import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

# F, S, G, U, D
F, S, G, U, D = map(int,input().split())
visited = [0]*F
visited[S] = 1
cnt = 0
while 1:
    if S == G:
        print(cnt)
        break
    if S+U <= G :
        if visited[S+U] == 0:
            S += U
            visited[S] = 1
            cnt += 1
    elif visited[S-D] == 0:
        S -= D
        cnt += 1
    if 0 not in visited:
        print('use the stairs')
        break