import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
import copy
n = int(input())

a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))
a_list.sort()

b_copy = sorted(b_list, reverse=True)
print(b_copy)
 