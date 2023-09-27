import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n,l = map(int,input().split())
h = list(map(int,input().split()))
h.sort()

for i in h:
    if l >= i:
        l += 1
    else:
        print(l)
        exit(0)
print(l)