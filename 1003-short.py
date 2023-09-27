import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")


T = int(input())
for _ in range(T):
    N = int(input())
    zero,one=1,0 # zero: 0개수, one: 1개수
    for i in range(N):
        zero,one = one,zero+one # zero와 one에 대해 피보나치적용
    print(zero,one)