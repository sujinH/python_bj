import sys
from itertools import combinations
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

n,m = map(int,input().split())
lst = [i for i in range(1,n+1)]

ans = []
while len(lst)>0:
    a = lst.pop(m-1)
    print(a)

print(ans)