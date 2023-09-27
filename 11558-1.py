import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

t = int(input())


for _ in range(t):
    n = int(input())
    stack = [0]*(n+1)
    for i in range(1,n+1):
        p = int(input())
        stack[i] = p

    for i in range(1,n+1):
        