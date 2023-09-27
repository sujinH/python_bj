import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

m = int(input())
ss = []
for i in range(m):
    s = list(map(str,input().split()))
    if len(s)>1:
        x = int(s[1])

    if s[0] == 'add':
        if x not in ss:
            ss.append(x)
    elif s[0] == 'remove':
        if x in ss:
            ss.remove(x)
    elif s[0] == 'check':
        if x in ss:
            print(1)
        else:
            print(0)
    elif s[0] == 'toggle':
        if x in ss:
            ss.remove(x)
        else:
            ss.append(x)
    elif s[0] == 'all':
        s=[i for i in range(1,21)]
    elif s[0] == 'empty':
        ss = []