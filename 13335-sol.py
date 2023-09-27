import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
 
bridge = [0] * w
time = 0
 
while bridge:
    time += 1
    bridge.pop(0)
    if trucks:
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)
    print(bridge)
print(time)