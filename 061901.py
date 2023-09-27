import sys
from collections import deque

# input = sys.stdin.readline
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n, k = map(int,input().split())

people = deque()
for i in range(1, n+1): people.append(i)
result = []
idx = k-1

while people :
    for _ in range(k-1):
        people.append(people.popleft())

    result.append(people.popleft())

print(str(result).replace('[','<').replace(']','>'))
