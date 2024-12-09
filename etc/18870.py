import sys
input = sys.stdin.readline

n = int(input())
coordinate = list(map(int, input().split(" ")))
new_coor = sorted(list(set(coordinate)))

dic = dict()
for i in range(len(new_coor)):
    dic[new_coor[i]] = i
# print(dic)
for i in coordinate:
    print(dic[i], end=" ")

