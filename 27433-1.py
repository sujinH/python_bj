import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n = int(sys.stdin.readline())

memo = {0:1, 1:1}

def sol(n):
    if n == 0:
        return print(memo[0])
    else:
        for i in range(1,n+1):
            if i in memo:
                memo[i+1] = memo[i]*(i+1)
    print(memo[n]) 
sol(n)