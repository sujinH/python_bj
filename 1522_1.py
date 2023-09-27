import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

s = list(input())
# 문자열 s의 a의 개수를 확인하여 윈도우를 만들어줌
a_cnt=s.count('a')
# 원형큐이므로 새로운 문자열 n_s = s + s[0:a_cnt]
s+=s[0:a_cnt]
l = 0; r=a_cnt
ans = sys.maxsize
while l<=r:
    x = s[l:l+a_cnt].count('b')
    l+=1
    ans = min(ans,x)

print(ans)