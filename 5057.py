import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

while 1:
    l = list(map(int,input().split()))
    l.sort()
    a, b, c = l[0], l[1], l[2]

    if a==0 and b==0 and c==0:
        break
    # 1. 삼각형의 조건이 되지 않는 경우
    if a+b <= c:
        print("Invalid")
        
    # 2. 세 변의 길이가 모두 같은 경우
    elif a == b ==c:
        print("Equilateral")
    # 4. 세 변의 길이가 모두 다르지만, 삼각형의 조건이 되는 경우
    elif a == b or b == c or c == a:
        print("Isosceles")

    else:
        print("Scalene")