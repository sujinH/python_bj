import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n=int(input())
m=int(input())
xs = list(map(int,input().split()))

max_v = 0
for i in range(m):
    if i == 0:
        max_v = xs[i] - 0
    
    if i == m-1:
        max_v = max(max_v,n-xs[m-1])

    if m>1 and i>0: #가로등이 2개이상이고, 2번째 가로등일 때,
        if (xs[i] - xs[i-1]) % 2 == 0:
            tmp=(xs[i] - xs[i-1]) // 2
        elif (xs[i] - xs[i-1]) % 2 != 0:
            tmp=(xs[i] - xs[i-1]) // 2 + 1

        max_v = max(max_v,tmp)
        

print(max_v)