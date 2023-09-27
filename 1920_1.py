import sys
import bisect
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
a.sort()

for x in b:
    l = 0; r = n-1
    flag = False
    while l <=r:
        mid = (l+r)//2
        if a[mid] == x:
            flag = True
            break
        elif a[mid] < x:
            l = mid + 1
        else:
            r = mid -1

    if flag == True:
        print(1)
    else:
        print(0)

