import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
arr = [i+1 for i in range(n)]
tmp = []
while len(arr) != 1:
    for idx, item in enumerate(arr):
        if idx % 2:
            tmp.append(item)
    arr = tmp
    tmp = []
print(arr[0])