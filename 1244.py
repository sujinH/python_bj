import sys
import copy
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

n = int(input())
state = list(map(int,input().split()))
m = int(input())
for i in range(m):
    a,b = map(int,input().split())
    if a == 1:
        for x in range(n):
            if (x+1) % b == 0:
                if state[x] == 0: state[x] = 1
                else: state[x] = 0
    
    elif a == 2:
        if state[b-1] == 0: state[b-1] = 1
        else: state[b-1] = 0

        for j in range(1,len(state)//2+1):
            if (b-1)-j < 0 or (b-1)+j >= len(state):
                break
            if state[b-1-j] == state[b-1+j]:
                if state[b-1-j] == 0:
                    state[b-1-j] = 1
                    state[b-1+j] = 1
                else:
                    state[b-1-j] = 0
                    state[b-1+j] = 0

            else:
                break

if len(state)<=20:
    print(*state, end = ' ')
else:
    tt = 0
    while tt<n:
        print(state[tt], end=' ')
        if len(state) % 20 == 0:
            if tt % 20 == 19 and tt != len(state)-1:
                print()
        else:
            if tt % 20 == 19:
                print()
        tt+=1

