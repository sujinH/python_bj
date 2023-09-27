import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n = int(sys.stdin.readline())
result = "YES"
stack = []
for _ in range(n):
    s = input()
    stack=[]
    result = "YES"
    for j in s:
        if j == "(":
            stack.append(j)
        else:
            if stack and stack[-1] =="(":
                stack.pop()
            elif not stack:
                result = "NO"
    if stack or result =="NO":
        print("NO")
    else:
        print("YES")        