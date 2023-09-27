import sys
import copy
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline


while 1:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break

    nlist = [int(input()) for _ in range(n)]
    mlist = [int(input()) for _ in range(m)]
    cnt =  0
    for x in nlist:
        start=0; end=m-1
        while start<=end:
            mid = (start+end)//2

            if mlist[mid] == x:
                cnt += 1
                break
            elif mlist[mid] < x:
                start = mid + 1

            else:
                end = mid -1

    print(cnt)