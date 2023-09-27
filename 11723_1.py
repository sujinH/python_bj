import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n = int(input())
for i in range(n):
    a = list(map(str,input().split()))
    if a[0] != 'empty' or a[0] != 'all':
        cmd,num = a[0],a[1]


    print(a)