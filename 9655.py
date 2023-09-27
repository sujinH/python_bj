import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
cnt = 0
while n>0:
    if n-3 >1:
        n-=3
    else:
        n-=1
    
    cnt+= 1

if cnt % 2 == 1:
    print('SK')
else:
    print('CY')