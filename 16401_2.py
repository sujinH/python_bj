import sys
import copy
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

m,n = map(int,input().split())
cookies = list(map(int,input().split()))
# cookies.sort()

start = 1; end = int(1e9)
ans =0
while start <= end:
    cnt = 0
    mid = (start+end)//2
    for x in cookies:
        cnt += x//mid

    if cnt >= m:
        ans = max(ans,mid)
        start = mid+1
    else:
        end = mid-1
print(ans)