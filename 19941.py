import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n, k = map(int,input().split())
s = list(input())
cnt =0

for j in range(n):
    if s[j] == 'P':
        for i in range(n):
            if s[i] == 'H':
                if abs(j-i) <= k:
                    s[i]='C'
                    cnt += 1
                    break

print(cnt)
