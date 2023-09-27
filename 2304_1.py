import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

n = int(input())
ware_house = [list(map(int,input().split())) for _ in range(n)]
ware_house.sort()
ware_house_map = [0]*(1001)
for i in range(n):
    ware_house_map[ware_house[i][0]] = ware_house[i][1]

start,end = ware_house[0][0],ware_house[-1][0]
tmp = ware_house_map[start]
for i in range(start,end+1):
    # 빈칸일 때는 전칸에 것을 그대로 들고올수있게
    if ware_house_map[i] < tmp:
        ware_house_map[i] = tmp
    else:
        tmp = ware_house_map[i]

tmp = ware_house_map[end]
for i in range(end,start-1,-1):
    # 빈칸일 때는 전칸에 것을 그대로 들고올수있게
    if ware_house_map[i] > tmp:
        ware_house_map[i] = ware_house[i]
    

print(ware_house_map)