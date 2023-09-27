import sys
import copy
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a,b = map(str,input().split())
    a = int(a,2)
    b = int(b,2)
    x=a+b
    x_10 = format(x,'b')
    print(x_10)