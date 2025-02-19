import sys
input = sys.stdin.readline
n = int(input())

member = []
for i in range(n):
    member.append(input().split())

member.sort(key= lambda x : int(x[0]))
for i, j in member:
    print(i,j)