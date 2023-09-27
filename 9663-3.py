import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

def check(n):
    for i in range(n):
        if row[i] == row[n] or abs(row[i]-row[n]) == i-n:
            return False
        return True

def dfs(n):
    global cnt
    if n == N:
        cnt += 1

    else:
        for i in range(N):
            row[n] = i
            if check(n):
                dfs(n+1)

N = int(input())
row = [0]
cnt = 0*N
dfs(0)
print(cnt)