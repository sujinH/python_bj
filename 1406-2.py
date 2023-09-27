import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

text1 = list(input())
len_text = len(text1)
# print(text1)
n = int(input())
idx = len(text1)
for i in range(n):
    m = list(map(str,input().split()))
    # print('idx: {}'.format(idx))
    if m[0]=='P':
        if idx == len(text1) :
            text1.append(m[1])
            idx += 1
        else:
            # 다시 확인
            text1.insert(idx,m[1])
            # text2 = text1[0:idx-1]
            # text3 = text1[idx-1:len(text1)]
            # text2.append(m[1])
            # text1 = text2 + text3

            
    elif m[0] == 'L':
        if idx != 0:
            idx -= 1
       
    elif m[0] == 'D':
         if idx != len(text1):
            idx = idx + 1

    elif m[0] == 'B':
        if len(text1)>0:
            if idx != 0:
                text1.remove(text1[idx-1])
                idx = idx - 1


    # print("{}: {}".format(i,text1))  

print(*text1,sep='')
