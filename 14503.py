import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def sol(cy,cx,cd):
    cnt = 0
    while 1:
    # 현재 칸이 아직 청소되지 않은경우
        grid[cy][cx]=2
        flag = 1
        cnt += 1
        while flag == 1: #청소x빈칸이 있는 경우
            for i in range(4):
                nd = (cd+3-i)%4
                ny,nx = cy+dy[nd],cx+dx[nd]
                if grid[ny][nx] == 0:
                    cy,cx,cd = ny,nx,nd
                    flag = 0
                    break
            else:
                by,bx = cy-dy[cd], cx-dx[cd]
                if grid[by][bx] == 1:
                    return cnt
                else:
                    cy,cx = by,bx

n,m = map(int,input().split())
r,c,d = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]

xx=sol(r,c,d)
print(xx)
