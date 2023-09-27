import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n=input()
stack=[]
tmp = " "
cnt=0
for x in n:
    
    if x == "(":
        stack.append(x)
    elif x == ")":
        if tmp == "(":
            stack.pop()
            cnt+=len(stack)
        elif tmp == ")" :
            stack.pop()
            cnt+=1

    tmp = x

print(cnt)