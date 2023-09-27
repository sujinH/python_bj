import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
global cnt1
cnt1=0
def fibo1(n):
    if n == 1 or n == 2:
        global cnt1
        cnt1 += 1
        return 1

    else:
        cnt1 += 1
        print(cnt1)
        return fibo1(n-1) + fibo1(n-2)

memo = [-1] * (n+1)
memo[0]=0;memo[1]=1;memo[2]=1

global cnt2
cnt2 = 0
def fibo2(n):
    global cnt2
    cnt2 +=1
    if n<2:
        return memo[n]
    else:
        for i in range(2, n+1):
            if memo[i] != -1:
                continue
            else:
                memo[i] = memo[i-1]+memo[i-2]

    return memo[n]


print(fibo1(n), fibo2(n))