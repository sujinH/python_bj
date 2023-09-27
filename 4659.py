import sys
import copy
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

s = ''
str_1_list = ['a','e','i','o','u']
while 1:
    s = input().strip()

    str_1 = 0 # 모음 개수
    str_2 = 0 # 자음 개수
    #첫번째 조건에 대한 flag
    flag1 = False
    flag2 = False
    flag3 = False

    # 종료조건 end
    if s == 'end':
        break

    state = ''
    state_cnt = 1
    prev = ''
    for x in s:
        if prev == x:
            if (prev == 'o' and x == 'o') or (prev == 'e' and x == 'e'):
                flag3 = False
            else:
                flag3 = True
                break
        if x in str_1_list:
            str_1 += 1
            flag1 = True
            if state == 'str_1':
                state_cnt += 1
            else:
                state_cnt = 1
            state = 'str_1'
        else:
            str_2 += 1
            if state == 'str_2':
                state_cnt += 1
            else:
                state_cnt = 1
            state = 'str_2'
        if state_cnt >=3:
            flag2 = True
            break
        prev = x

    if flag2 == True:
        print("<{}> is not acceptable.".format(s))
        continue
    if flag3 == True:
        print("<{}> is not acceptable.".format(s))
        continue
    if flag1 == False:
        print("<{}> is not acceptable.".format(s))
    
    else:
        print("<{}> is acceptable.".format(s), sep='')