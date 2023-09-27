import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
s = list(map(str,sys.stdin.readline().rsplit()))
n=len(s)
m=int(sys.stdin.readline())
cursor = n
for i in range(m):
    list_a = list(map(str,sys.stdin.readline().split()))

    if list_a[0] == "L":
        if cursor >-1:
            cursor -= 1
    elif list_a[0] == "D":
        if cursor < n:
            cursor += 1
    elif list_a[0] == "B":
        if cursor > 0:
            u = s[cursor-1]
            s.remove(u)
            cursor -= 1
    elif list_a[0] == "P":
        if cursor > -1:
            s.insert(cursor, list_a[1])
            cursor+=1
        elif cursor == -1:
            s.insert(0, list_a[1])
            cursor = 1

for i in s:
    print(i, end='')

    