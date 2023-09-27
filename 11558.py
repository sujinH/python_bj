import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    k = 0
    for x in range(1,N+1):
        target = int(sys.stdin.readline())
        if target != N:
            k+=1
        elif target == N:
            k+=1
            print(k)
            break
        else:
            print(0)