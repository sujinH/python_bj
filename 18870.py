import sys
import copy
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline
# -10, -9, 2, 4, 4
n = int(input())
s = list(map(int,input().split()))
# [-10, -9, 2, 4]
a = sorted(list(set(s)))
# {-10: 0, -9: 0, 2: 0, 4: 0}
dict_a = dict.fromkeys(a,0)

for i in range(len(a)):
    dict_a[a[i]] = i

for i in s:
    print(dict_a[i])
