import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

def up(y,x,n):
    y-=1
    n+=1
    return y,x,n

def right(y,x,n):
    x+=1
    n+=1
    return y,x,n

def down(y,x,n):
    y+=1
    n+=1
    return y,x,n

def left(y,x,n): 
    x-=1
    n+=1
    return y,x,n

def draw(y,x,t):
    num = 1
    graph[y][x] = num

    for n in range(1,t+1):
        if n%2 == 0 :
            continue
        
        y,x = up(y,x,num)
        graph[y][x] = num

        for i in range(n-2):
            y,x = right(y,x,num)
            graph[y][x] = num

        for i in range(n-1):
            y,x = down(y,x,num)
            graph[y][x] = num

        for i in range(n-1):
            y,x = left(y,x,num)
            graph[y][x] = num

t = int(input())
find = int(input())
graph = [[0]*t for _ in range(t)]

draw(t//2,t//2,t)
print(graph)