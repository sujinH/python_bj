import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())



stack = []
for _ in range(n):
    m = int(input())
    stack.append(m)

max_n = max(stack)

dp = [0]*max_n

dp[0] = 1
dp[1] = 1
dp[2] = 1

for i in range(3,max_n):
    dp[i] = dp[i-2]+dp[i-3]

for j in stack:
    print(dp[j-1])