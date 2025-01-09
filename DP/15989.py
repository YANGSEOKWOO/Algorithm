# 1,2,3 더하기 4

import sys
input = sys.stdin.readline

t = int(input())

# 최대 n 값 계산


# DP 테이블 초기화
dp = [[0] * 4 for _ in range(10001)]
for k in range(4):
    dp[0][k] = 1  # 합이 0일 경우

for i in range(1,10001):
    for j in range(1,4):
        dp[i][j] = dp[i][j-1]
        if i >= j:
            dp[i][j] += dp[i-j][j]


# 결과 출력
for n in range(t):
    a = int(input())
    print(dp[a][3])
