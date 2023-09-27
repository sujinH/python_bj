import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

m, n = map(int,input().split())
cookie = list(map(int,input().split()))
cookie.sort()
l=1; r=cookie[n-1]
ans = 0
while l <= r:
    mid = (l+r)//2
    cnt = 0
    for x in cookie:
        cnt += x // mid
    if cnt >= m:
        l = mid+1
        ans = mid

    else:
        r = mid-1

print(ans)