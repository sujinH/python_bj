import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

a_n, b_n = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
a_dict = dict.fromkeys(a,0)
for x in b:
    l=0; r=a_n-1
    while l <= r:
        mid = (l+r)//2
        if a[mid] == x:
            a_dict[x] += 1
            break

        elif a[mid] < x:
            l = mid + 1
        
        else:
            r = mid - 1
cnt = 0

for k,v in a_dict.items():
    if v == 0:
        cnt += 1
if cnt == 0:
    print(0)
    exit()
else:
    print(cnt)

for k,v in a_dict.items():
    if v == 0:
        cnt += 1
        print(k, end=' ')
