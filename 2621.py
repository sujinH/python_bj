import sys
from collections import deque
from collections import Counter
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

# 카드: 빨 / 파 / 노 / 녹  색별로 1~9 까지 총 36장
# 36장 중 5장을 뽑고 규칙으로 정수를 계산
arr = []
for i in range(5):
    a, b = map(str, input().split())
    a = a + b
    arr.append(a)
arr.sort()

red = []
blue = []
yellow = []
green = []

cnt = 0
# ['B2', 'B3', 'B7', 'R1', 'Y7']
for i in arr:
    s = i[0:1]
    if  s in 'R':
        n = int(i[1:2])
        red.append(n)

    elif  s in 'B':
        n = int(i[1:2])
        blue.append(n)

    elif  s in 'Y':
        n = int(i[1:2])
        yellow.append(n)

    elif  s in 'G':
        n = int(i[1:2])
        green.append(n)

array = []
array.append(red)
array.append(blue)
array.append(yellow)
array.append(green)
print("arr: {}".format(arr))
print(array)
result = []
for i in range(len(array)):
    if len(array[i]) == 5:
        if array[i][4] - array[i][0] == 4:
            result.append(array[i][4] + 900)
        elif array[i][4] - array[i][0] != 4:
            result.append(array[i][4] + 600)
    
    elif arr[i][1:2]:
    

# print(arr[0][1:2])