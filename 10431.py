import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

def BubbleSort(List):
    global cnt
    for i in range(len(b)-1,0,-1):
        for j in range(i):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
                cnt += 1

    return cnt

T = int(input())
for _ in range(T):
    a, *b = map(int,input().split())
    cnt = 0
    print(a, BubbleSort(b))