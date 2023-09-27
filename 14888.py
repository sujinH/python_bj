import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")


n = int(input())
a = list(map(int,input().split()))
num = list(map(int,input().split()))

op=[]
for i in range(4):
    for j in range(num[i]):
        if i ==0:
            op.append('+')
        elif i ==1:
            op.append('-')
        elif i ==2:
            op.append('*')
        elif i ==3:
            op.append('//')

print(op)
