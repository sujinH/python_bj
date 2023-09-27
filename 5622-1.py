import sys
# input = sys.stdin.readline
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

arr = {'A':2, 'B':2, 'C':2, 'D':3, 'E':3, 'F':3, 'G':4, 'H':4,
       'I':4, 'J':5, 'K':5, 'L':5, 'M':6, 'N':6, 'O':6, 'P':7,
       'Q':7, 'R':7, 'S':7, 'T':8, 'U':8, 'V':8, 'W':9, 'X':9,
       'Y':9, 'Z':9}

st = input()
sum_st = 0
for i in st:
    sum_st += (arr[i]+1)

print(sum_st)