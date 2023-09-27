import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(sys.stdin.readline())
count = 1
stack = []
result = []
temp = True
for i in range(n):
    x = int(sys.stdin.readline())

    while count <= x:
        stack.append(count)
        result.append("+")
        count += 1

    if stack[-1] == x:
        stack.pop()
        result.append("-")
    else: 
        temp = False
        # print("NO")
        break

if temp == False:
    print("NO")
else:
    for i in result:
        print(i)