import sys
from collections import deque

# input = sys.stdin.readline
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n, k = map(int,input().split())

stack = [i for i in range(1, n+1)]
people = deque(stack)
idx = k-1
result = []
while people:

    for _ in range(k-1):
        people.append(people.popleft())

    result.append(people.popleft())

print(str(result).replace('[','<').replace(']','>'))