# n의 생성자 => 결국 어떤 수의 분해합을 했을 때, n이 나오는 수

import sys
input = sys.stdin.readline

n = int(input())

anw = 0
flag = False

for i in range(1, n):
    num = i
    for j in str(num):
        num += int(j)
    if (num == n):
        anw = i
        flag = True
        break
if flag:
    print(anw)
else:
    print('0')