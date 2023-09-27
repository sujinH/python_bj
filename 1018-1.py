import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n,m = map(int,input().split())

graph = [ list(map(str,input())) for _ in range(n)]

w_panel = [
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBwBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW'
]

b_panel = [
'BWBWBWBW',
'WBWBWBWB',
'BWBwBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB'
]

ans = []
for y in range(n):
    for x in range(m):
        w_cnt = 0
        b_cnt = 0
        if 0<=y<n and 0<=y+7<n:
            if 0<=x<m and 0<=x+7<m:
                for j in range(y,y+8):
                    for i in range(x,x+8):
                        print(y,x)
                        print(j,i)
                        if graph[y][x] != w_panel[j][i]:
                            w_cnt += 1
                        elif graph[y][x] != b_panel[j][i]:
                            b_cnt += 1
                print(w_cnt,b_cnt)
                ans.append(min(w_cnt,b_cnt))

print(ans)
print(min(ans))