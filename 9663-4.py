import sys
input = sys.stdin.readline

def dfs(n):
    global cnt
    if n == N:
        cnt += 1
        return
    
    for i in range(N):
        if ch1[n+i] == ch2[n-i] == ch3[n] == ch4[i] == 0:
                ch1[n+i] = ch2[n-i] = ch3[n] = ch4[i] = 1
                dfs(n+1)
                ch1[n+i] = ch2[n-i] = ch3[n] = ch4[i] = 0
    

N = int(input())
ch1 = [0]*(N*2)
ch2 = [0]*(N*2)
ch3 = [0]*(N+1)
ch4 = [0]*(N+1)
cnt = 0
dfs(0)
print(cnt)