import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = list(map(str,sys.stdin.readline().strip()))
stack = []
result = 0
for i in range(len(n)):
    if n[i] == "(":
        stack.append("(")
    
    else: # ")"
        if n[i-1] == "(":
            stack.pop()
            result += len(stack)

        elif n[i-1] == ")":
            stack.pop()
            result += 1

print(result)