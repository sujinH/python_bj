import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
m,n = map(int,sys.stdin.readline().split())

# m과 n사이의 소수를 모두 구하기 
# 소수란 나와 그 값으로만 나누어지는 수

ans=[0 for i in range(n+1)]

for i in range(m,n+1):
    count = 0
    for j in range(1,i):
        if i%j == 0:
            count+=1
            ans[i] += count

for i in range(len(ans)):
    if ans[i] == 1:
        print(i)

