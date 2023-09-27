import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
s = sys.stdin.readline()

# 알파벳은 26개.. ord('a') = 97 / chr(97) = 'a' // 97(a)~122(z)

alph = [-1 for i in range(26)]

for i in range(len(s)):
    if s[i] == "\n":
        break
    if alph[ord(s[i])-97] == -1:
        alph[ord(s[i])-97] = i


print(*alph)

# print(ord('a'))
# print(ord('z'))
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 6 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 (o)