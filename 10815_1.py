import sys
import bisect
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

def Binary_search(n,s_card,m,cards):
    for x in s_card:
        l = 0; r = m-1
        while l<=r:
            mid = (l+r)//2
            if cards[mid] == x:
                cards_dict[x] += 1
                break
            elif cards[mid] < x:
                l = mid + 1
            else:
                r = mid - 1




n = int(input())
s_card = list(map(int,input().split()))

m = int(input())
cards = list(map(int,input().split()))
cards_dict = dict.fromkeys(cards,0)
cards.sort()
ans = [0]*(m)
Binary_search(n,s_card,m,cards)
print(*cards_dict.values())