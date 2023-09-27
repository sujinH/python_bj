import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n = int(sys.stdin.readline())
arr = []
global cnt
cnt=0
def recursion(n):
    s=''
    for i in range(n):
        for j in range(n):
            if i==1 and j ==1:
                s += ''.join(" ")
            else:
                s += ''.join("*")
        s += ''.join("\n")

    print(s)
recursion(3)
# def shape(n):
#     cnt +=1
#     return recursion(n,cnt,)
# shape(n)