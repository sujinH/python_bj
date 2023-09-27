import sys
import bisect
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
a.sort()
m = int(input())
b = list(map(int,input().split()))

for x in b:
    left, right = 0, len(a)-1
    flag = False
    while left <=right:
        mid = (left+right) //2
        if a[mid] == x:
            flag = True
            break
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1  

    if flag == True:
        print(1)
    else:
        print(0)

