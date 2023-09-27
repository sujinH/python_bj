import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
q =deque()
n = int(input())

arr = list(map(int,input().split()))
stack = []
ans = [-1 for _ in range(n)]
temp = []
count = 0
q.append(arr[0])
for i in range(1,len(arr)):
    while q and q[-1] < arr[i]:
        q.popleft()
        ans[count] = arr[i]
        count += 1
    q.append(arr[i])
print(*ans)
# for i in range(len(arr)):
#     while stack and arr[stack[-1]] < arr[i]:
#         ans[stack.pop()] = arr[i]
#     stack.append(i)
# print(*ans)