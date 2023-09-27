import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def dfs(n):
    if len(lst) == k:
        print(*lst)
        return 
    global prev
    for j in range(n,N[0]+1):
        if N[j] not in lst:
            lst.append(N[j])
            dfs(j+1)
            lst.pop()

k=6
while True:
    N = list(map(int,input().split()))
    if N[0] == 0:
        break
    
    lst = []
    dfs(1)
    print()