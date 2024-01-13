import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
card = list(map(int, input().split(" ")))

sum = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n):
            num = card[i] + card[j] + card[k]
            if m >= num and num > sum:
                sum = num
print(sum)