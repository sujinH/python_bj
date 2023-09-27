import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [1]*10
    
    for i in range(1,n):

        temp = arr.copy()
        arr[0] = temp[7]
        arr[1] = temp[2] + temp[4]
        arr[2] = temp[1] + temp[5] + temp[3]
        arr[3] = temp[6] + temp[2]
        arr[4] = temp[1] + temp[5] + temp[7]
        arr[5] = temp[4] + temp[2] + temp[6] + temp[8]
        arr[6] = temp[3] + temp[5] + temp[9]
        arr[7] = temp[4] + temp[8] + temp[0]
        arr[8] = temp[5] + temp[7] + temp[9]
        arr[9] = temp[6] + temp[8]
            
    print(sum(arr))