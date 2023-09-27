import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n = int(sys.stdin.readline())
stack=[]
for i in range(n):
    num = int(sys.stdin.readline())
    # stack.append(num)
    if stack and num==0:
        stack.pop()
    if num != 0:
        stack.append(num)
        
result=0
for i in stack:
    result += i
print(result)