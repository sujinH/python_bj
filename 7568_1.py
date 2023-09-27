import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

n = int(input())
students = [list(map(int,input().split())) for _ in range(n)]

for now_w,now_h in students:
    rank = 1
    for w,h in students:
        if now_w < w and now_h < h:
            rank += 1
    
    print(rank)