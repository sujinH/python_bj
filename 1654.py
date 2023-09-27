import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

k,n = map(int,input().split())
arr = [int(input()) for _ in range(k)]
arr.sort()

l,r= 0,arr[k-1]
while l<=r:
    mid = (l+r)//2
    cnt = 0
    for a in arr:
        cnt += a//mid

    if cnt >= n:
        l = mid + 1

    if cnt < n:
        r = mid - 1


print(r)