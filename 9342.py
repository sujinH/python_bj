import sys
import re
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline
n = int(input())
check = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(n):
    t = input()
    if check.match(t) == None:
        print('Good')
    else:
        print('Infected!')