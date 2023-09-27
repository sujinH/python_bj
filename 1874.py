import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n = int(sys.stdin.readline())
stack = []
result = ''
memo = []
for _ in range(n):
    num = int(sys.stdin.readline())
    for i in range(1,num+1):
        if i not in stack and i not in memo:
            stack.append(i)
            result += ''.join("+")
        if i == num:
            if stack[-1] == num:
                memo.append(stack.pop())
                result += ''.join("-")

        elif not stack:
            result = "NO"
            break
if stack or result == "NO":
    print(result)
else:
    for i in result:
        print(i)

