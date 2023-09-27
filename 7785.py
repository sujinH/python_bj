import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

n = int(sys.stdin.readline())
people = {}
for i in range(n):
    a, b = map(str, sys.stdin.readline().split())

    if b == "enter":
        people[a] = 1
    elif b == "leave":
        people.pop(a)
# people.sort(reverse=True)
people = sorted(people, reverse=False)

# print(people)
for i in people:
    print(i)
