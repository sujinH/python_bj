import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n =int(sys.stdin.readline())
sang = list(map(int,sys.stdin.readline().split()))
m =int(sys.stdin.readline())
check_sang = list(map(int,sys.stdin.readline().split()))

ans = [0]*len(check_sang)