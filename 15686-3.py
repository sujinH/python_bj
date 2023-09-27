import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline
from itertools import combinations

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

chicken = []
home = []
# graph를 돌면서 2이면 치킨 1차원 배열에 좌표등록, 1이면 홈 1차원 배열에 좌표등록
for y in range(n):
    for x in range(n):
        if arr[y][x] == 2:
            chicken.append((y,x))
        elif arr[y][x] == 1:
            home.append((y,x))

result = []

for chi in combinations(chicken,m):
    tmp = 0
    home_chi_dis_min = []
    for i in range(len(home)):
        y1,x1 = home[i][0], home[i][1]
        min_chi = []
        for j in range(m):
            y2, x2 = chi[j][0], chi[j][1]
            distance = abs(y2-y1) + abs(x2-x1)
            min_chi.append(distance)
        home_chi_dis_min.append(min(min_chi))
    result.append(sum(home_chi_dis_min))
        # result.append(tmp)
print(min(result))