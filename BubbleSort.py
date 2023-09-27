import sys

a="900 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916 917 918 919"
lista = list(map(int,a.split()))
cnt = 0
for i in range(len(lista)-1,0,-1):
    for j in range(len(lista[:i])):
        if lista[j]>lista[j+1]:
            lista[j],lista[j+1]= lista[j],lista[j+1]
            cnt += 1

print(cnt)
    

