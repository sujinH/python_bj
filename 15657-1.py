import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

n,m = map(int,input().split())
s = list(map(int,input().split()))
s.sort()
arr=[]
def dfs(idx):
    if len(arr) == m:
        print(*arr)
        return 

    for i in range(idx,n):
        arr.append(s[i])
        dfs(idx)
        arr.pop()


dfs(0)