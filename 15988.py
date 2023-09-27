import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
    


for _ in range(n):
    a = int(input())
    dp = [0]*(a+1)

    for j in range(1,a+1):
        if a == 1:
            print(1)
            break
        if a == 2:
            print(2)
            break
        if a == 3:
            print(4)
            break
        
        dp[j]