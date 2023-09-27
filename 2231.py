import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(sys.stdin.readline())
rslt= []
for i in range(1,n):
    text_str= list(str(i))
    text_int = list(map(int,text_str))
    # print(sum(text_int))
    if sum(text_int) + i == n:
        rslt.append(i)
        break
if len(rslt) == 0:
    print(0)
else:   
    print(rslt[0])