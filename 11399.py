import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
s = list(map(int,input().split()))
s.sort()
ans = 0
tmp = 0
# [1 2 3 3 4]
for i in range(len(s)):
    ans += s[i]

    tmp += ans

print(tmp)