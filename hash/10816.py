import sys
input = sys.stdin.readline

n = int(input())
number_card = list(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))

anw = dict()
for i in card:
    anw[i] = 0

for i in number_card:
    if anw.get(i) != None:
        anw[i]+=1

for i in card:
    print(anw[i], end=" ")