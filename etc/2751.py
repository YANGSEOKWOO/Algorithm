import sys
input = sys.stdin.readline

n = int(input())
arr_n = [int(input()) for _ in range(n)]
arr_n.sort()
for i in arr_n:
    print(i)