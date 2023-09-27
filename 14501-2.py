import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [0]*(n+1)
for i in range(n-1,-1,-1):
    if arr[i][0] + i <= n:
        dp[i] = max(dp[i+1] , arr[i][1]+dp[i+arr[i][0]])
    else:
        dp[i] = dp[i+1]
print(dp)