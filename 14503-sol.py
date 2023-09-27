import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

d = [0,1,2,3]
dy = [-1,0,1,0]
dx = [0,1,0,-1]

n,m = map(int,input().split())
r,c,d = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def solve(cy,cx,dr):
    cnt = 0
    while 1:
        grid[cy][cx] = 2
        cnt+=1
        flag = 1

        while flag == 1:
            for nd in ((dr+3)%4, (dr+2)%4, (dr+1)%4, (dr+0)%4):
                ny,nx = cy+dy[nd], cx+dx[nd]
                if grid[ny][nx] == 0:
                    cy,cx,dr = ny,nx,nd
                    flag = 0
                    break

            else:
                by,bx = cy-dy[dr], cx-dx[dr] 
                if grid[by][bx] == 1:
                    return cnt
                else:
                    cy,cx = by,bx

                
       

cc = solve(r,c,d)
print(cc)