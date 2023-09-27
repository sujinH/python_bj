import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

while True:
    a,b,c = map(int,input().split())

    if a == 0 and b == 0 and c == 0:
        break

    if a >= b+c or b >= c+a or c >= a+b:
        print("Invalid")
    elif a == b and b == c and c == a:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")

    