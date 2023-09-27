import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(n,cnt1,cnt2):
    if len(lst) == L:
        if cnt1 >= 1 and cnt2 >=2:
            print(*lst,sep ='')
            return
    
    for j in range(n,C):
        if num[j] in check_alpha: # 모음 카운트
            cnt1 += 1
        elif num[j] not in check_alpha: # 자음 카운트
            cnt2 += 1

        lst.append(num[j])
        dfs(j+1,cnt1,cnt2)
        lst.pop()
        if num[j] in check_alpha: # 모음 카운트
            cnt1 -= 1
        elif num[j] not in check_alpha: # 자음 카운트
            cnt2 -= 1

L,C = map(int,input().split())
num = list(map(str,input().split()))
check_alpha = ['a','e','i','o','u']
num.sort()
lst = []
cnt1 = 0
cnt2 = 0
dfs(0,cnt1,cnt2)
