import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
cnt = 0
tmp = 1

if n == 1:
    print(1)
    exit(0)

while tmp < n:
    tmp += cnt * 6
    cnt += 1

print(cnt)