import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
# input = sys.stdin.readline

arr = []
ans = ''
lines = sys.stdin.readlines()
for x in lines:
    txt =x.rstrip()
    ans += ' '
    ans += ''.join(x)
arr = list(map(str, ans.split()))

leng = len(arr)
nm = {'Re':0,'Pt':0,'Cc':0,'Ea':0,'Tb':0,'Cm':0,'Ex':0}

for i in range(len(arr)):
    if arr[i] in nm:
        nm[arr[i]] += 1

for i, (key, val) in enumerate(nm.items()):
    print(key,val, format(val/leng, ".2f"))

print("Total {}".format(leng),end=' ')
print(format(1.00, ".2f"))
