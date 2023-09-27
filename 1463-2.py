import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
dp[n] = 0
for i in range(n-1,0,-1):
    dp[i] = dp[i+1]+1
    if i%3 == 0:
        dp[i] = max(dp[i//3], dp[i+1])
    elif n%2 == 0:
        dp[i] = max(dp[i//2], dp[i+1])

print(dp)
