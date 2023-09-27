import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

num = int(input())
dp = [0]*(num+1)

dp[1] = 1
for j in range(2,num+1):
    if j == 2:
        dp[j] = 1
    else:
        dp[j] = dp[j-1] + dp[j-2]

print(dp[num])