import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
dp = [[0]*3 for _ in range(n)]
dp[0][0] = 1
dp[0][1] = 1
dp[0][2] = 1
for i in range(1,n):
    dp[i][0] = dp[i-1][0]+dp[i-1][1]+dp[i-1][2]
    dp[i][1] = dp[i-1][0]+dp[i-1][2]
    dp[i][2] = dp[i-1][0]+dp[i-1][1]

print(dp[n-1][0]+dp[n-1][1]+dp[n-1][2])
