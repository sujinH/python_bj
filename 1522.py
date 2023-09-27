import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

s = list(input().strip())
leng = len(s)
a_cnt = s.count('a')
s+=s[:a_cnt]
left = 0
ans = sys.maxsize
while left <= leng:
    x = s[left:left+a_cnt].count('b')
    left+=1
    ans = min(ans,x)
print(ans)