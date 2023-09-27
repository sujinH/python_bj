import sys
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")

T = int(input())
for _ in range(T):
    password = [1]*10
    N = int(input())
    for i in range(1, N):
        newPass = password
        # 길이가 N인 비밀번호의 갯수는 인접한 숫자의 길이가 N-1인 비밀번호의 갯수와 같다.
        password[0] = newPass[7]
        password[1] = newPass[2] + newPass[4]
        password[2] = newPass[1] + newPass[3] + newPass[5]
        password[3] = newPass[2] + newPass[6]
        password[4] = newPass[1] + newPass[5] + newPass[7]
        password[5] = newPass[2] + newPass[4] + newPass[6] + newPass[8]
        password[6] = newPass[3] + newPass[5] + newPass[9]
        password[7] = newPass[4] + newPass[8] + newPass[0]
        password[8] = newPass[5] + newPass[7] + newPass[9]
        password[9] = newPass[6] + newPass[8]
        
    print(sum(password)%1234567)