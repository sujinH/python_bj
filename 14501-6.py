import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n=int(input())
t = [0]*n
p = [0]*n
dp = [0]*(n+1)
for i in range(n):
    x,y = map(int,input().split())
    t[i] = x
    p[i] = y

for i in range(n-1,-1,-1):
    if t[i] + i <= n:
        dp[i] = max(dp[i+1],dp[i+t[i]] + p[i] )
    else:
        dp[i] = dp[i+1]

print(dp[0])