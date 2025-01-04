import sys
input = sys.stdin.readline

n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))

dic = dict()
for i in arr_n: 
    dic[i] = 1

for i in arr_m:
    if dic.get(i,0) != 1:
        print(0)
    else:
        print(1)
