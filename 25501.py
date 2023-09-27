import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n = int(sys.stdin.readline())

cnt = 0
memo = [0,0]
def recursion(s, l, r, cnt):
    if l>=r:
        cnt +=1
        memo[0]=1; memo[1]=cnt
        return memo
    elif s[l] != s[r]:
        cnt +=1
        memo[0]=0; memo[1]=cnt
        return memo
    else:
        cnt +=1
        return recursion(s,l+1,r-1,cnt)

def isPalindrome(s):
    cnt = 0
    return recursion(s, 0, len(s)-1, cnt)

for _ in range(n):
    strings = sys.stdin.readline().strip()
    result = isPalindrome(strings) 
    print(result[0], result[1])