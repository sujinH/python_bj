import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n,m = map(int,input().split())

graph = [ list(map(str,input())) for _ in range(n)]

w_panel = [
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW'
]

b_panel = [
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB'
]

ans = []
for y in range(n):
    for x in range(m):
        b_cnt = 0
        w_cnt = 0
        if 0<=x<m and 0<=y<n:
            if 0<=x+7<m and 0<=y+7<n:
                for j in range(8):
                    for i in range(8):
                        if graph[y+j][x+i] != b_panel[j][i]:  
                            b_cnt += 1
                        if graph[y+j][x+i] != w_panel[j][i]:    
                            w_cnt += 1
                ans.append(min(b_cnt,w_cnt))
print(min(ans))