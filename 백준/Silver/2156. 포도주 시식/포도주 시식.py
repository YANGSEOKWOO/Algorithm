n = int(input())

anw = [int(input()) for _ in range(n)]  # 사용자 입력값들
grape_juice = [0] + anw # 인덱스 1부터 시작하도록 0 추가

dp= [0]*(n+1)

if n == 1:
    print(grape_juice[1])
elif n == 2:
    print(grape_juice[1] + grape_juice[2])
else:
    dp[1] = grape_juice[1]
    dp[2] = dp[1] + grape_juice[2]
    for i in range(3, n+1):
        dp[i]  = max(dp[i-2] + grape_juice[i], dp[i-3] + grape_juice[i-1] + grape_juice[i], dp[i-1])
    print(max(dp))