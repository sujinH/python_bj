import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n,k = map(int,input().split())
arr = [0] * 100001
for j in range(n+1,len(arr)):
    if j == k:
        print(arr[j])
        break

    arr[j] = arr[j-1] + 1
    if j//2 >= n and j % 2 == 0:
        arr[j] = min(arr[j], arr[j//2])
    print(arr[j])
