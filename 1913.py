import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

def up(y,x,num):
    y-=1
    num+=1
    graph[y][x] = num
    return y, x, num

def right(y,x,num):
    x+=1
    num+=1
    graph[y][x] = num
    return y, x, num

def down(y,x,num):
    y+=1
    num+=1
    graph[y][x] = num
    return y, x, num

def left(y,x,num):
    x-=1
    num+=1
    graph[y][x] = num
    return y, x, num

def draw(y,x,t):
    num = 1
    center_y, center_x=y,x
    for j in range(1,t+1):
        if j % 2 != 0:
            if j == 1:
                graph[y][x] = num
                continue
            y,x = center_y,center_x
            y,x,num = up(y,x,num)
            for i in range(j-2):
                y,x,num = right(y,x,num)
            for i in range(j-1):
                y,x,num = down(y,x,num)
            for i in range(j-1):
                y,x,num = left(y,x,num)
            for i in range(j-1):
                y,x,num = up(y,x,num)
            
            center_y,center_x = center_y-1,center_x-1
            



n = int(input())
find = int(input())
graph = [[0]*n for _ in range(n)]
draw(n//2,n//2,n)

for j in range(n):
    for i in range(n):
        print(graph[j][i], end=' ')
        if graph[j][i] == find:
            t_j,t_i=j,i
    print() 

print(t_j+1,t_i+1)