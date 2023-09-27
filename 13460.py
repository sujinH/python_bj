import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n,m = map(int,input().split())
graph = [list(map(str,input().rstrip())) for _ in range(n)]
visited = []
dy = [-1,1,0,0]
dx = [0,0,-1,1]
q = deque()

ry,rx,by,bx =0,0,0,0

for j in range(n):
    for i in range(m):
        if graph[j][i] == 'R':
            ry, rx = j, i
        if graph[j][i] == 'B':
            by, bx = j, i

q.append([ry,rx,by,bx,1])
visited.append([ry,rx,by,bx])

def move(y,x,j,i):
    count = 0
    while graph[y+j][x+i] != '#' and graph[y][x] != 'O':
        y+=j
        x+=i
        count+=1
    return y,x,count


def bfs():
    while q:
        ry,rx,by,bx,cnt = q.popleft()

        if cnt > 10:
            break

        for i in range(4):
            nry, nrx, rcnt = move(ry,rx,dy[i],dx[i])
            nby, nbx, bcnt = move(by,bx,dy[i],dx[i])

            if graph[nby][nbx] == 'O':
                continue

            if graph[nry][nrx] == 'O':
                return cnt

            if nry == nby and nrx == nbx:
                if rcnt>bcnt:
                    nry -= dy[i]
                    nrx -= dx[i]
                else:
                    nby -= dy[i]
                    nbx -= dx[i]

            if [nry,nrx,nby,nbx] not in visited:
                visited.append([nry, nrx, nby, nbx])
                q.append([nry, nrx, nby, nbx,cnt+1])

    return -1

print(bfs())