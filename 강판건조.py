import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input2.txt","r")

for _ in range(2):
    n = int(input())
    heights = list(map(int, input().split()))

    count = 0
    for i in range(n):
        for j in range(i+1, n-i):
            if heights[i] < heights[j]:
                break
            else:
                if heights[i] == heights[j]:
                    count+=1

    print(count)