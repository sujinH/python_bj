import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

s = list(map(str,input()))
s.sort()
arr = []
for i in range(len(s)):
    if i % 2 == 0:
        arr.append(s[i])

print(arr+arr[::-1])