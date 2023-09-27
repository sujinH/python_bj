import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
arr = []
for i in range(11):
    b=list(map(int,input().split()))
    arr.append(b)
cnt = 0
for y in range(11):
    for x in range(10):
        if arr[y][x] == 0:
            cnt += 1

print(cnt)