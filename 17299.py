import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))
max_num = max(arr)
ans = [-1 for _ in range(n)]
#NGF를 구하려고 함
# 목표: 가장 왼쪽에 있으면서 본인보다 횟수가 많은 애들을 찾는것
idx = [0 for _ in range(max_num+1)]
for i in range(len(arr)):
    idx[arr[i]] += 1

    
stack = []
for i in range(n):
    for j in range(i+1,n):
        if idx[arr[i]] < idx[arr[j]]:
            ans[i] = arr[j]
            break

print(*ans) 