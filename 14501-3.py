import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
tmp = [list(map(int,input().split())) for _ in range(n)]
dp = [0]*(n+1)
for i in range(n-1,-1,-1):
    if i + tmp[i][0] <= n:
        dp[i] = max(dp[i+tmp[i][0]]+tmp[i][1], dp[i+1])

print(dp)
