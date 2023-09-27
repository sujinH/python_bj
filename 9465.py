import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    #  입력받기
    n = int(input())
    s = [list(map(int,input().split())) for _ in range(2)]
    dp = [[0]*(n+1) for _ in range(2)]
    dp[0][n-1] = s[0][n-1]
    dp[1][n-1] = s[1][n-1]
    # dp[0][n-2] = s[0][n-2]
    # dp[1][n-2] = s[1][n-2]


    for i in range(n-2,-1,-1):
        dp[0][i] = max(s[0][i] + dp[1][i+1], s[0][i] + dp[0][i+2], s[0][i] + dp[1][i+2])
        dp[1][i] = max(s[1][i] + dp[0][i+1], s[1][i] + dp[0][i+2], s[1][i] + dp[1][i+2])


    print(max(dp[0][0], dp[1][0]))
    # print(dp[0][0],dp[0][1])
