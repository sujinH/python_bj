import sys
import copy
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline
grid = [list(input().strip()) for _ in range(5)]

# 이다솜 s파 임도연 y파
tmp = []
def dfs(idx):
    if idx == 7:
        print(tmp)
        return
    
    for i in range(idx):
        tmp.append(grid[idx][i])
        dfs(idx)
        tmp.pop()

dfs(0)