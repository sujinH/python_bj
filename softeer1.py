import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n, m = map(int,input().split())

car = []
for i in range(n):
    x = input()
    car.append(x)
car.sort()
so = [0]*9
av = [0]*9
gr = [0]*9

for _ in range(m):
    x = list(map(str,input().split()))
    x[1] = int(x[1])
    x[2] = int(x[2])
    if x[0] == 'avante':
        for j in range(x[1],x[2]):
            av[j-9] = 1
    elif x[0] == 'sonata':
        for j in range(x[1],x[2]):
            so[j-9] = 1
    elif x[0] == 'grandeur':
        for j in range(x[1],x[2]):
            gr[j-9] = 1

reservation = []
for i in range(n):
    if car[i] == 'avante':
        if av[i] == 1:
            reservation.append()

print(reservation)        

# cnt = 0
# for i in range(n):
#     print('Room {}:'.format(car[i]))
#     if car[i] == 'avante':
