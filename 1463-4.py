import sys
input = sys.stdin.readline
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
flag = True
dp = [0]*(n+1)
for i in range(1,n):
    if i % 3 == 0:
        if dp[i-1] > dp[i//3]:
            dp[i] = dp[i // 3] + 1
    elif i % 2 == 0:
        if dp[i-1] > dp[i//2]:
            dp[i] = dp[i // 2] + 1
    else:
            dp[i] = dp[i-1] + 1       

print(dp)