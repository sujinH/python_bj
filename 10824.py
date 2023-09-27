import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
a,b,c,d = map(str,sys.stdin.readline().split())

print(int(a+b) + int(c+d))