import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline
from collections import deque

n = int(input())
p=[list(map(int,input().split())) for _ in range(n)]
rank = []
ans =[]
for j in p:
    rank = 1
    for i in p:
        if j[0] < i[0] and j[1] <i[1]:
            rank += 1
    ans.append(rank)

print(*ans)