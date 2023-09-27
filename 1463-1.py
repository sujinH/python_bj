import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())

dp = [0]*(n+1)
if n == 1:
    print(1)
    exit(0)

for i in range(2,n+1):
    dp[i] = dp[i-1]+1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    elif i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[n])