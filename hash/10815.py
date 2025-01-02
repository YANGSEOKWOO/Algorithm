import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())
num_m = list(map(int, input().split()))

dic = dict()

for i in num:
    dic[i] =1

for i in num_m:
    if dic.get(i, 0) != 1:
        print(0, end=" ")
    else:
        print(1, end=" ")