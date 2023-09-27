import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

T = int(input())

for _ in range(T):
    n = int(input())
    dp = [0]*(n+1)

    dp[1]=1; dp[2]=2; dp[3]=4
    if 0<=n<4:
        exit(0)

    for j in range(4,n+1):
        dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
    print(dp[n])