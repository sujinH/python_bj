import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
n=int(input())

for _ in range(n):
    a,*lista = map(int,input().split())
    cnt = 0
    for i in range(len(lista)-1,0,-1):
        for j in range(len(lista[:i])):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]= lista[j+1],lista[j]
                cnt += 1

    print(a,cnt)
    

