import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

s = input()
memo = {}
for i in s:
    if ord(i) >=97:
        i = chr(ord(i)-32)
    if i not in memo:
        memo[i] = 1
    else:
        memo[i] += 1

m = 0; ans = ''
for (k,v) in memo.items():
    if m < v:
        m = v; ans = k

    if m == v and k != ans:
        ans2 = k

for (k,v) in memo.items():
    if ans != k and v == m:
        print('?')
        exit(0)
print(ans)