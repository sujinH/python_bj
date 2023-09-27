import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def sol1(ans1):
    global total
    global total_val
    for i in range(N):
        x = total + ans1[i][0]
        if x > K:
            result.append(total_val)
            return
        total += ans1[i][0]
        total_val += ans1[i][1]
        if total == K:
            result.append(total_val)
            return
def sol2(ans2):
    global total1
    global total_val1
    for i in range(N):
        x = total1 + ans2[i][0]
        if x > K:
            result.append(total_val1)
            return
        total1 += ans2[i][0]
        total_val1 += ans2[i][1]
        if total == K:
            result.append(total_val1)
            return
N,K = map(int,input().split())
ans = []
for i in range(N):
    w, v = map(int,input().split())
    ans.append((w,v))
ans1 = sorted(ans, key=lambda x: x[0])
ans2 = sorted(ans, key=lambda x: x[1], reverse=True)
# print(ans1)
# print(ans2)
total = 0
total_val = 0
total1 = 0
total_val1 = 0
result = []
sol1(ans1)
sol2(ans2)
print(max(result))