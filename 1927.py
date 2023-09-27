import sys
import heapq
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(arr,x)
    elif x == 0 and not arr:
        print(0)
    else:
        a = heapq.heappop(arr)
        print(a)

