import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n = int(input())



def fac(n):
    if n <=1:
        return 1
    return n * fac(n-1)

