import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

H,W = map(int,input().split())
maps = list(map(int,input().split()))
ans = 0
for idx in range(1,W-1):
    left_max = max(maps[:idx])
    right_max = max(maps[idx+1:])

    lower_one = min(left_max,right_max)

    if lower_one > maps[idx]:
        ans += lower_one - maps[idx]

print(ans)
