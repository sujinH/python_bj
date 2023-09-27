import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

inp1 = list(map(str,sys.stdin.readline()))
inp2 = list(map(str,sys.stdin.readline()))
cnt = 0

d_1 = deque(inp1)
d_2 = deque(inp2)
num = 0
while len(d_1)>len(d_2):
    cnt = 0
    for i in range(len(d_2)):
        if d_1[i] == d_2[i]:
            cnt += 1
        elif d_1[i] != d_2[i]:
            break
    if cnt == len(d_2):
        for _ in range(len(d_2)):
            d_1.popleft()
        num += 1
    
print(num)