import sys
from collections import Counter
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

n = int(input())
nlist= list(map(int,input().split()))
m = int(input())
mlist = list(map(int,input().split()))

dic = dict()
for i in nlist:
    if i not in dic:
        dic[i] = 1
    elif i in dic:
        dic[i] += 1

for k in mlist:
    if dic[k]:
        print(dic[k], end=' ')
    else:
        print(0, end=' ')