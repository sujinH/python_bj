import sys
from collections import deque
from itertools import combinations
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n, m = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))

chicken = []
home = []
for j in range(n):
    for i in range(n):
        if graph[j][i] == 2:
            chicken.append((j,i))
        elif graph[j][i] == 1:
            home.append((j,i))

print(chicken)
print(home)
result = 9999 
for chi in combinations(chicken, m):
    tmp = 0
    for h in home:
        dis = 99999
        for k in range(m):
            dis = min(dis,abs(h[0]-chi[k][0]) + abs(h[1]-chi[k][1]))
        tmp += dis
    result = min(result,tmp)
            # print(h[0],chi[k][0])
print(result)