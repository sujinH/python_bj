import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

m,n= map(int,sys.stdin.readline().split())

for i in range(m,n+1):
    
    if i % 2 != 0 and i % 3 != 0:
        print(i)
    elif i == 2 or i == 3 :
        print(i)