import sys
input = sys.stdin.readline

n = int(input())

# n : 1000, 시간제한 1초

num = [int(input()) for _ in range(n)]

num.sort()

for i in num:
    print(i)
