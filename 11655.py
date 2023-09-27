import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n = sys.stdin.readline()
# a~z : 97~122 / A~Z : 65~90
# B = 66
result = ''
for i in range(len(n)):
    # 소문자일경우
    if 97<=ord(n[i])<=122:
        if ord(n[i])-13>=97:
            tmp = chr(ord(n[i])-13)
            result += ''.join(tmp)
        else:
            tmp = chr(ord(n[i])+13)
            result += ''.join(tmp)
    
    elif 65<=ord(n[i])<=90:
        if ord(n[i])-13>=65:
            tmp = chr(ord(n[i])-13)
            result += ''.join(tmp)
        else:
            tmp = chr(ord(n[i])+13)
            result += ''.join(tmp)

    else:
        result +=n[i]
print(result)