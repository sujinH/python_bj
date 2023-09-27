import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

a, b = map(int, input().split())
result = []
def solution(arr1, arr2):
    array = []
    cnt1 = 0; cnt2 = 0
    for _ in range(a):
        x = input()
        array.append(x)
    print(array)

    start1 = 0; end1 = b
    start2 = 0; end2 = a

    for i in range(8):
        for j in range(start1,end1):
            if array[i][j] == arr1[i][j]:
                cnt1 += 1

            if array[i][j] == arr2[i][j]:
                cnt2 += 10.
                


    result.append(min(cnt1, cnt2))

# arr1 =[
# ['WBWBWBWB'],
# ['BWBWBWBW'],
# ['WBWBWBWB'],
# ['BWBWBWBW'],
# ['WBWBWBWB'],
# ['BWBWBWBW'],
# ['WBWBWBWB'],
# ['BWBWBWBW'],
# ]

# arr2 =[
# ['BWBWBWBW'],
# ['WBWBWBWB'],
# ['BWBWBWBW'],
# ['WBWBWBWB'],
# ['BWBWBWBW'],
# ['WBWBWBWB'],
# ['BWBWBWBW'],
# ['WBWBWBWB'],
# ]

arr1 =[
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
]
arr2 =[
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
]

solution(arr1, arr2)
print(result)
# ['BWBWBWBW'],
# ['WBWBWBWB'],
# ['BWBWBWBW'],
# ['WBWBWBWB'],
# ['BWBWBWBW'],
# ['WBWBWBWB'],
# ['BWBWBWBW'],
# ['WBWBWBWB'],
