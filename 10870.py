import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n = int(sys.stdin.readline())

def fibo(n):
    if n == 0:
        return 0
    else:
        if n == 1:
            return 1
        else:
            return fibo(n-1) + fibo(n-2)



print(fibo(n))