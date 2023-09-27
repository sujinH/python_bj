import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n, w, l = map(int, input().split())
truck = list(map(int, input().split()))
truckq = deque(truck)
bridge = [0] * w
bridge_q = deque(bridge)
cnt = 0
for i in range(n):
    for j in range(w):
        bridge_q.popleft()
        
        if len(truckq) == 0:
            if len(bridge_q) > 0:
                bridge_q.append(0)
                cnt+=1

            else:
                break

        else:
            if sum(bridge_q) + truckq[0] < l:
                bridge_q.append(truckq.popleft())
                cnt += 1
            elif sum(bridge_q) + truckq[0] > l:
                bridge_q.append(0)
                cnt += 1
            
            

print(cnt)
 

# for i in range(n):
#     for j in range(w):
#         if bridge_q[0] == 0:
#             bridge_q[0] = truckq.popleft

#         else:
#             if bridge_q[0] + truckq[0] <= l:
#                 bridge_q.popleft()
#                 bridge_q.append(truckq.popleft())
#             elif bridge_q[0] +truckq[0] > l:
#                 bridge_q.append(bridge_q.popleft())

#         print(bridge_q)
        