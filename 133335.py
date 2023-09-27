import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")


# truck에서 popleft해서 제일 앞에 있는 트럭을  
#  다리 맨 왼쪽의 0을 하나 빼고 오른쪽에 낑겨넣음
# 만약 다리위의 truck무게의 sum이 l 보다 작다면
# 만약 크다면? -> 다리에 있는애들만 왼쪽으로 한칸씩넘기고
# 맨오른쪽에 0 추가

n,w,l = map(int,input().split())
t = list(map(int,(input().split())))
b = [0] * w
truck = deque(t)
bridge = deque(b)
cnt =0
while True:
    if truck:

        if  sum(bridge) - bridge[0] + truck[0] <= l:
            bridge.popleft()
            bridge.append(truck.popleft())
            cnt += 1
            

        elif sum(bridge) - bridge[0] + truck[0] > l:
            bridge.popleft()
            if sum(bridge) == 0:
                bridge.append(truck.popleft())
            elif sum(bridge) > 0:
                bridge.append(0)
            cnt += 1
    
    elif not truck:
        bridge.popleft()
        bridge.append(0)
        cnt += 1
    if len(truck) == 0 and sum(bridge) == 0:
        break

print(cnt)