import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())
arr = [i for i in range(1,n+1)]

for _ in range(n):
    tmp = []
    # 1회에 한해 arr에서 숫자를 뽑아 tmp에 저장해둠
    for i in range(n):
        if i % 2 == 1 and arr[i] != 0:
            tmp.append(arr[i])
            x = arr[i]
        elif i == 1 and arr[i] == 0:
            y = x
    arr = [0]*n
    for j in range(len(tmp)):
        arr[j] = tmp[j]
# =============================================
# tmp = []
# for i in range(n):
#     if i % 2 == 1 and arr[i] != 0:
#         tmp.append(arr[i])

# arr = [0]*n
# for j in range(len(tmp)):
#     arr[j] = tmp[j]
# print(arr)
# =============================================
if  n == 1:
    y = 1
print(y)
