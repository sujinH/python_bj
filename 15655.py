import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

def dfs(n):
    if len(lst)==M:
        print(*lst)

    for j in range(n,N):
        if s[j] not in lst:
            lst.append(s[j])
            dfs(j+1)
            lst.pop()

N,M = map(int,input().split())
s = list(map(int,input().split()))
s.sort()
lst = []

dfs(0)