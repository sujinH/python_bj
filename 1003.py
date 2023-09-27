import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

t = int(input())

memo = {0:(1,0), 1:(0,1)}

tmp_0 = 0
tmp_1 = 1
for i in range(t):
    
    x = int(input())
    if x in memo:
        tmp_0 = memo[x][0] # 1
        tmp_1 = memo[x][1] # 0
        print(tmp_0, tmp_1) 
    else:
        for j in range(x):
            if ｊ in memo:
                