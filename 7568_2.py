import sys
import copy
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

n = int(input())
info = [list(map(int,input().split())) for _ in range(n)]
info_s = sorted(info,key=lambda x: (x[0],x[1]))
# [[46, 155], [55, 185], [58, 183], [60, 175], [88, 186]]

for j in info:
    cur_w,cur_h = j
    cnt = 1
    for i in info_s:
        w,h = i
        if cur_w < w and cur_h <h:
            cnt += 1

    print(cnt)
