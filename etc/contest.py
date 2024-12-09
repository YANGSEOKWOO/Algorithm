import sys

a, b = map(int, sys.stdin.readline().split())
a_card = list(map(int, sys.stdin.readline().split()))
b_card = list(map(int, sys.stdin.readline().split()))

ans = 0
for k in range(min(a, b), 0, -1):
    for i in range(a-k+1):
        temp = []
        for j in range(i+k):
            if a_card[j] in b_card:
                temp.append(a_card[j])
        flag = True
        for j in range(k):
            if temp[j] != b_card[b_card.index(temp[0])+j]:
                flag = False
                break
        if flag:
            ans = k
            print(ans)
            exit()
print(ans)