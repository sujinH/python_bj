import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n1 = int(input())
s1= list(map(int,input().split()))

n2 = int(input())
s2= list(map(int,input().split()))

# 딕셔너리 key & value는 카운트로 세팅
dict_s2 = {}
for i in range(n2):
    dict_s2[s2[i]] = 0

for i in range(n1):
    if s1[i] in dict_s2:
        dict_s2[s1[i]] += 1

for i in range(n2):
    if dict_s2[]