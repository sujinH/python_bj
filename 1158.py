import sys
from collections import deque

sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
    data = list(map(str,sys.stdin.readline().split()))
    if data[0] == "push":
        data[1] = int(data[1])
        q.append(data[1])
    
    elif data[0] == "pop":
        if q:
            x = q.popleft()
            print(x)
        else:
            print(-1)

    elif data[0] == "size":
        print(len(q))

    elif data[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif data[0] == "front":
        print(q[0])

    elif data[0] == "back":
        print(q[-1])