import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())

arr = [i for i in range(1, n+1)]
tmp = []
while len(arr) != 1:
    for j in range(n):
        if j%2 == 1:
            tmp.append(arr[j])
    for _ in range(n-len(tmp)):
        tmp.append(0)
    arr = tmp
    tmp = []
    cnt = 0

    if arr[1] == 0 and arr[0] !=0:
        print(arr[0])