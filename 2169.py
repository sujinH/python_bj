import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
