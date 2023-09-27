import sys
from collections import deque
import heapq
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key = lambda x: x[1])
print(arr)
cnt = 0 
mh = []
for i in arr:
    while mh and mh[0] <= i[1]:
        heapq.heappop(mh)
    heapq.heappush(mh,i[2])
    cnt = max(cnt, len(mh))
print(cnt)
