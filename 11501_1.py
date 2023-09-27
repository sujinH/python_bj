import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    days = list(map(int,input().split()))
    max = days[-1]
    ans = 0
    for i in range(n-2,-1,-1):
        if days[i] < max:
            ans += max - days[i]
        
        else:
            max = days[i]

    print(ans)