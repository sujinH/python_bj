import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

a, b = map(int,input().split())
cards = list(map(int,input().split()))
cards.sort()
result = []
# 브루트포스
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            # print("i: {}, j: {}, k:{}".format(i,j,k))
            if cards[i] + cards[j] + cards[k]<=b:
                result.append(cards[i] + cards[j] + cards[k])
result.sort()
print(result[-1])
