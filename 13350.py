import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
price = list(map(int,input().split()))
distance = list(map(int,input().split()))

for i in range(n):
    find_min = min(price)
