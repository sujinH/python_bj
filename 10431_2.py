import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

p= int(input())
for _ in range(p):
    a,*T = map(int,input().split())
    cnt=0
    for j in range(len(T)-1,0,-1):
        for i in range(len(T[:j])):
            if T[i] > T[i+1]:
                T[i],T[i+1] = T[i+1],T[i]
                cnt+=1
    
    print(cnt)