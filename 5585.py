import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

money = int(input())

money = 1000-money
coin = [500,100,50,10,5,1]
cnt = 0
for i in range(len(coin)):
    if money>0:
        cnt += (money // coin[i])
        money %= coin[i]

print(cnt)