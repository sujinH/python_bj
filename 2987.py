import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

r, c = map(int,input().split())
n = 2
maps = [input() for _ in range(r)]
print(maps)
cnt = 0
result = [0] * 5
for i in range(r-n+1):
    for j in range(c-n+1):
        findB = False
        for a in range(2):
            for b in range(2):
                if maps[a+i][b+j] == '#':
                    findB = True
                    break
                elif maps[a+i][b+j] == 'X':
                    cnt += 1
            if findB == True:
                break
        if findB == True:
            findB = False
        else:
            result[cnt] += 1
        cnt = 0

for i in range(5):
    print(result[i])