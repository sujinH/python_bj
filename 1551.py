import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

a,b = map(int,input().split())

arr = list(map(int,input().split(',')))

if b ==0:
    print(*arr,sep=',')

    exit(0)

tmp = arr[0]
ans =[]
for j in range(b):
    if j !=0:
        arr = ans.copy()
    tmp = arr[0]
    ans =[]
    for i in range(1,len(arr)):
        ans.append(arr[i] - tmp)
        tmp = arr[i]
print(*ans, sep=',')

