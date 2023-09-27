import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
max_num = max(nums)
idx = [0 for i in range(max_num+1)]
for i in range(len(nums)):
    idx[nums[i]] += 1 

stack = []
ans = [-1 for i in range(len(nums))]
for i in range(len(nums)):
    while stack and idx[nums[stack[-1]]] < idx[nums[i]]:
        ans[stack.pop()] = nums[i]
    stack.append(i)

print(*ans)