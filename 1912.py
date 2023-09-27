import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
s = list(map(int,input().split()))

dp = [0]*(n+1)
dp[1] = max(s)

for j in range(1,n):
    s[j] = max(s[j], s[j-1]+s[j])


print(s)