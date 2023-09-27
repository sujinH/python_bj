import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n,k = map(int,input().split())
s = list(map(int,input().split()))
cnt = 0
for i in range(len(s)-1,0,-1):
    cnt +=1
    for j in range(len(s[:i])):
        if s[j] > s[j+1]:
            s[j] , s[j+1] =  s[j+1], s[j] 

    if cnt == k:
        break

print(*s)