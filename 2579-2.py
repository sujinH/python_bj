import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

# 입력값 세팅
n = int(input())
s = [int(input()) for _ in range(n)]

memo = [0]*n


if n == 1:
    print(s[n-1])
else:
    memo[0] = s[0]
    memo[1] = memo[0]+s[1]
    for i in range(2,n):
        memo[i] = max(memo[i-3]+s[i-1]+s[i], memo[i-2]+s[i])

    print(memo[-1])