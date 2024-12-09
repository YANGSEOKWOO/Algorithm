import sys
input = sys.stdin.readline

# 수 n개가 주어졌을 때, i번째 부터 j번째 수 까지 합을 구하는 프로그램
# 시간복잡도 => M * 슬라이싱(N) => 1초를 넘는다
# nlogn으로 풀어야 하는 문제

N, M = map(int, input().split(" "))
N_number = list(map(int, input().split(" ")))
acc = []
temp = 0
for i in N_number:
    temp += i
    acc.append(temp)

for k in range(M):
    i, j = map(int, input().split(" "))
    if i-2 <0:
        print(acc[j-1])
    else:
        print(acc[j-1]-acc[i-2])
