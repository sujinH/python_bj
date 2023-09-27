import sys
from collections import deque
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")


shapes = [
    [[1, 1], 
     [1, 1]], # 네모

    [[1, 1, 1, 1]], # 길쭉이 1
    [[1], [1], [1], [1]], # 길쭉이 2

    [[1, 1, 1], 
     [0, 1, 0]], # T-모양 1
    [[0, 1, 0], 
     [1, 1, 1]], # T-모양 2
    [[1, 0], 
     [1, 1], 
     [1, 0]], # T-모양 3
    [[0, 1], 
     [1, 1], 
     [0, 1]], # T-모양 4

    [[1, 1, 0], 
     [0, 1, 1]], # 꺽은 모양 1
    [[0, 1, 1], 
     [1, 1, 0]], # 꺽은 모양 2
    [[1, 0], 
     [1, 1], 
     [0, 1]], # 꺽은 모양 3
    [[0, 1], 
     [1, 1], 
     [1, 0]], # 꺽은 모양 4

    [[1, 1, 1], 
     [0, 0, 1]], # L-모양 1
    [[0, 0, 1], 
     [1, 1, 1]], # L-모양 2
    [[1, 1, 1], 
     [1, 0, 0]], # L-모양 3
    [[1, 0, 0], 
     [1, 1, 1]], # L-모양 4

    [[1, 1], 
     [1, 0], 
     [1, 0]], # L-모양 5
    [[1, 1], 
     [0, 1], 
     [0, 1]], # L-모양 6
    [[1, 0], 
     [1, 0], 
     [1, 1]], # L-모양 7
    [[0, 1], 
     [0, 1], 
     [1, 1]]  # L-모양 8
]

def place(s, i, j, A):
    h, w = len(s), len(s[0])
    val = 0
    for r in range(h):
        for c in range(w):
            val += s[r][c] * A[i + r][j + c]
    return val

def maximize(s, n, m, A):
    h, w = len(s), len(s[0])
    opt = 0
    for i in range(n - h + 1):
        for j in range(m - w + 1):
            opt = max(opt, place(s, i, j, A))
    return opt

def solve(n, m, A):
    opt = 0
    for k in range(len(shapes)):
        opt = max(opt, maximize(shapes[k], n, m, A))
    return opt 

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, m, A))
