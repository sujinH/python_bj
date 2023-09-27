import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline
def dfs(n,lst):
    global res
    if len(lst) == N//2:
      
        A = 0
        B = 0
        for j in range(N):
            for i in range(N):
                if v[j] and v[i]:
                    A += graph[j][i]
                elif not v[j] and not v[i]:
                    B += graph[j][i]
        res = min(res,abs(A-B))    
        return res
        # ans.append(min(res,abs(A-B))) 
    
    for j in range(n,N):
        if not v[j]:
            v[j] = 1
            dfs(j+1,lst + [j])
            v[j] = 0

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
v = [0]*N
res = 2175000000
dfs(0,[])
print(res)