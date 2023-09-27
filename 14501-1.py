import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

N = int(input())
T = [0]*N
P = [0]*N
# arr = [list(map(int,input().split())) for _ in range(n)]
for i in range(N):
    T[i], P[i] = map(int,input().split())

dp = [0]*(N+1)
for n in range(N-1,-1,-1):
    if n + T[n] <= N:
        dp[n] = max(dp[n-1], P[n] + dp[n+T[n]])
    else:
        dp[n] = dp[n+1]
print(dp)


