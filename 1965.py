import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
s = list(map(int,input().split()))

dp = [0] * n
dp[0] = s[0]
cnt = 0
for i in range(1,n):
    if s[i] > dp[i-1]:
        cnt +=1

print(cnt-1) 