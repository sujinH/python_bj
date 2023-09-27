import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline
from collections import deque
from itertools import permutations


N = int(input())
graph = [i for i in range(1,N+1)]

cnt = 1
for i in permutations(graph,N):
    print(i[0], end= ' ')