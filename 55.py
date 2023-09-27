import sys
import math
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n = int(sys.stdin.readline())
grid = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]


temp_max = 0
temp_min = math.inf
for i in range(n):
    for j in range(n):
        if grid[i][j] > temp_max:
            temp_max = grid[i][j]
        if grid[i][j] < temp_min:
            temp_min = grid[i][j]

print(temp_max)
print(temp_min)