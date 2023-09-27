import sys
import copy
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

n = int(input())
target = list(input().strip())
answer = 0

for j in range(n-1):
    word = list(input().strip())
    compare = copy.deepcopy(target)
    cnt = 0
    for x in word:
        if x in compare:
            compare.remove(x)
        else:
            cnt += 1

    if len(compare)<2 and cnt<2:
        answer+=1

print(answer)
