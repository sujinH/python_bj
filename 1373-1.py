import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

stack = list((map(int,sys.stdin.readline())))
leng = len(stack)
arr = []
for i in range(leng):
    t = i%3
    tmp = stack.pop()*(2**t)
    arr.append(tmp)

cnt=0
result=0
for i in range(len(arr)):
    if cnt<3:
        result += arr[cnt]
        cnt+=1

    print(result)