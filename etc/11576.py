import sys
input = sys.stdin.readline


a, b= map(int, input().split())
m = int(input())
num = list(map(int, input().split()))


def ten(arr, a):
    n = len(arr)-1
    anw = 0
    for i in range(len(arr)):
        anw += arr[n-i]*(a**i)
    return anw

def arith(number , b):
    anw = []
    while number != 0:
        anw.append(number%b)
        number = number//b
    return anw[::-1]

anw = arith(ten(num,a),b)
for i in anw:
    print(i, end =" ")

# 1. 10진수로 바꾸기
# 2. b진수로 바꾸기


# 17 *2  = 34 + 16 = 50
# 8*6 +2 = 50