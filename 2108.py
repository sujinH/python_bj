import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
s = [int(input()) for _ in range(n)]
s.sort()
arr = [0]*(max(s)+1)
print(round(sum(s)/n))
if n%2 != 0:
    print(s[n//2+1])
else:
    print(s[n//2])

for i in s:
    arr[i] += 1


print('asdf')
print(arr)
