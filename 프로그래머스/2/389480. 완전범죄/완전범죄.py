# 1. a: 내림차순으로 정렬
# 2. a가 같다면, b는 오름차순
import math

def solution(info, n, m):
    INF = float('inf')
    items = len(info)
    # dp[i][j]: i개의 물건을 처리했을 때, B의 흔적이 j일 때의 A의 누적 흔적
    dp = [[INF]*m for _ in range(items+1)]
    dp[0][0] = 0
    
    for i in range(1, items+1):
        a, b = info[i-1]
        for j in range(m):
            
            # A가 i를 골랐을 때
            check_a = dp[i-1][j] + a
            if n > check_a:
                dp[i][j] = min(dp[i][j], check_a)
            
            # B가 i를 골랐을 때
            if m > j+b:
                dp[i][j+b] = min(dp[i][j+b], dp[i-1][j])
    k = min(dp[len(info)])
    if k == INF:
        return -1
    return k