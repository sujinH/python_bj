import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")


def sol(cnt):
    global r

    for i in range(n):
        if a[i] >= b:
            r = a[i] - b
            cnt += 1
            cnt += r//c
            if r%c != 0:
                cnt += 1

        else:
            cnt += 1
    return cnt

n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())
r = 0
print(sol(0))
