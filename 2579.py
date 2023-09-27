import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
s = [int(input()) for _ in range(n)]

dp = [0]*n

if len(s)<=2:
    print(sum(s))
else:
    dp[0] = s[0]
    dp[1]=s[0]+s[1]
    for i in range(2,n):
        dp[i] = max(dp[i-3]+s[i-2]+s[i], dp[i-3]+s[i-1]+s[i])

    print(dp[-1])        