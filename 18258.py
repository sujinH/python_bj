import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(sys.stdin.readline())

q = deque()

for i in range(n):
    arr = list(map(str,sys.stdin.readline().split()))
    # push
    if arr[0] == 'push':
        q.append(arr[1])
    # pop: leftpop이고, stack이 비었으면 -1출력
    elif arr[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    # size
    elif arr[0] == 'size':
        print(len(q))
    # empty: 비었으면 1 , 존재하면 0
    elif arr[0] == 'empty':
        if q:
            print(0)
        elif not q:
            print(1)
    elif arr[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif arr[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)     
    