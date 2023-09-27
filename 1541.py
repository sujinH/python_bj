import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

nums = list(map(str,input()))

# 전처리 과정
tmps = ''
stack = []
flag = 0
for i in nums:
    if i != '+' and i != '-':
        tmps += ''.join(i)
    elif i == '+' :
        if flag == 0:
            stack.append(tmps)
            stack.append(i)
            tmps = ''
        elif flag == 1:
            stack.append(tmps)
            stack.append('-')
            tmps = ''
    elif i == '-':
        stack.append(tmps)
        stack.append(i)
        tmps = ''
        flag = 1

if len(tmps) > 0:
    stack.append(tmps)

tmp = ""
# print(stack)
for i in stack:
    if i.isdecimal() == True:
        i = str(int(i))
    tmp += i

print(eval(tmp))