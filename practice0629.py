import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
# n = int(input())
# rslt=''
# a = list(map(str,input().split()))

# 1번 풀이
a, b = map(str, input().split())
a = list(a)
b = list(b)
a = a[::-1]
b = b[::-1]
result=''
result2=''

for i in range(len(a)):
    result += str(a[i])
result2=''
for i in range(len(b)):
    result2 += str(b[i])
print(max(result,result2))
# 2번 풀이
# reverse_a='';reverse_b=''
# a, b = map(str, input().split())
# reverse_a += ''.join(reversed(a))
# reverse_b += ''.join(reversed(b))
# print(max(reverse_a,reverse_b))