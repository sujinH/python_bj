import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

num = input()
memo = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0,}
dict(memo)
stack = []
for i in num:
    x=int(i)
    if x in memo:
        memo[x] += 1
    # elif x not in memo:
    #     memo[x] = 1
if (memo[6]+memo[9]) % 2 == 0:
    print(max(max(memo.values())-memo[6]-memo[9], (memo[6]+memo[9])//2) )
elif (memo[6]+memo[9]) % 2 == 1:
    print(max(max(memo.values())-memo[6]-memo[9], (memo[6]+memo[9])//2 + 1))

# print((memo[6]+memo[9])//2 + 1)
# print(max(memo.values(), (memo[6]+memo[9])//2 + 1))