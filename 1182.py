import sys
import math
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(n):
    global cnt
    if len(lst)>0 and sum(lst) == S:
        cnt += 1
    
    for j in range(n,N):
        lst.append(nums[j])
        dfs(j+1)
        lst.pop()

cnt = 0
N,S = map(int,input().split())
nums = list(map(int,input().split()))
lst=[]
dfs(0)
print(cnt)