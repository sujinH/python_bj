import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))

memo=[0]*(n)

if len(s)<=2:
    print(sum(s))
else:
    memo[0] = s[0]
    memo[1] = s[0]+s[1]
    for i in range(2,n):
        memo[i] = max(memo[i-3]+s[i-1]+s[i], memo[i-2]+s[i])

print(memo[-1])