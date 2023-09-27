import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

# 1번은 한쪽 2번은 양쪽 3번은 직각 4번은 위좌우 5번은 사각

n,m = map(int,input().split())
graph = [[list(map(int,input().split()))] for _ in range(n)]
visited = [[0]*m for _ in range(n)] 

