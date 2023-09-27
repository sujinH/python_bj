import sys
import copy
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

n = int(input())
cnt = 0
cow = {}
for j in range(n):
    num, flag = map(int,input().split())
    if num in cow:
        if cow[num] != flag:
            cow[num]=flag
            cnt += 1
    else:
        cow[num] = flag

print(cnt)