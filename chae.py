import sys
import math
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

a, b=map(int,input().split())

for i in range(a, b+1):
    if i == 1:
        continue

    for j in range(2,int(math.sqrt(i)) + 1):
        if i % j == 0:
            break

    else: 
        print(i)