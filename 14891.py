import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

s=[]

for i in range(4):
    tmp = deque()
    tmp.append(list(map(int,input())))
    s.append(tmp)
k = int(input())
# print(s[0])
for _ in range(k):
    idx, dir = map(int,input().split())
    print(s[idx-1].popleft())
    # if dir == -1:
    #     s[idx-1].append(s[idx-1].popleft())

    # elif dir == 1:
    #     s[idx-1].insert(0,s[idx-1].pop())
