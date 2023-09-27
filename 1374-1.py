import sys
# input = sys.stdin.readline
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
import heapq

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])

s = []
for i in arr:
    while s and s[0]<i[1]:
        heapq.heappop(s)
    heapq.heappush(s,i[2])