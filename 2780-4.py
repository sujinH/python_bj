import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(input())

for _ in range(n):
    x = int(input())
    arr = [1] * 10
    for i in range(x):
        tmp = arr.copy()
        if i>0:
            arr[0] = tmp[7]
            arr[1] = tmp[2] + tmp[4]
            arr[2] = tmp[1] + tmp[3] + tmp[5]
            arr[3] = tmp[2] + tmp[6]
            arr[4] = tmp[1] + tmp[5] + tmp[7]
            arr[5] = tmp[2] + tmp[4] + tmp[6] + tmp[8]
            arr[6] = tmp[3] + tmp[5] + tmp[9]
            arr[7] = tmp[0] + tmp[4] + tmp[8]
            arr[8] = tmp[5] + tmp[7] + tmp[9]
            arr[9] = tmp[6] + tmp[8]

    print(sum(arr)%1234567)