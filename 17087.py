import sys
import math
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n, s = map(int,sys.stdin.readline().split())
sisters_x = list(map(int,sys.stdin.readline().split()))
distance = [0]*n
stack = []
a=''
for i in range(n):
    distance[i] = abs(s - sisters_x[i])
    

for i in range(len(distance)):
    if i==0:
        tmp=1
        distance[i]=math.gcd(tmp,distance[i])
        stack.append(distance[i])
    else:
        m = math.gcd(stack[-1],distance[i])

print(m)