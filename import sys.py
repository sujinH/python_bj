import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
height = list(map(int,input().split()))

cnt = 0
for i in range(n):
    for j in range(i+1,n):
        if height[i] < height[j]:
            break
        elif height[i] == height[j]:
            cnt +=1
print(cnt)