import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

H,W=[*map(int,input().split())]
blocks=list(map(int,input().split()))

print(H,W)
print(blocks)