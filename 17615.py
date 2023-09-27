import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(sys.stdin.readline())
arr = list(map(str,sys.stdin.readline()))
arrR = arr.copy()
arrB = arr.copy()
cntR = 0
R = arrR.count("R")
B = arrB.count("B")
for i in range(n):
    if arrR[-1] == "R":
        arrR.pop()
        cntR += 1
    elif arrR[-1] == "B":
        break
cntB = 0
for i in range(n):
    if arrB[-1] == "B":
        arrB.pop()
        cntB += 1
    elif arrB[-1] == "R":
        break
    
print(min(R-cntR,B-cntB))