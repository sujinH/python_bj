import sys
import math
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

a, b = map(int,input().split())
try:
    if 1<=a<=1000 and 1<=b<=1000:
        if a<=b:
            ans1 = b-a-1
            print(ans1)
        elif a>b:
            a,b = b,a
            ans1 = b-a-1
            print(ans1)

    if 1<=a<=math.pow(10,15) and 1<=b<=math.pow(10,15):
        if b-a <= math.pow(10,5):
            for i in range(a+1,b):
                    print(i, end=' ')
except:
     sys.exit()


# if 1<=a<1000 and 1<=b<1000:
#     ans1 = b-a-1
#     print(ans1)

# if 1<=a<=math.pow(10,15) and 1<=b<=math.pow(10,15):
#     if b-a
#     for i in range(a+1,b):
#         print(i, end=' ')