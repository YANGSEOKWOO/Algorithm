'''
동전 1, 10, 25, 100
'''

dp = [0]*101
dp[100] = 1
for i in range(1,100):
    if i >= 100:
        dp[i] = min(dp[i-1], dp[i-10], dp[i-25], dp[i-100]) + 1
    elif i >= 25:
        dp[i] = min(dp[i-1], dp[i-10], dp[i-25]) + 1
    elif i >= 10:
        dp[i] = min(dp[i-1], dp[i-10]) + 1
    else:
        dp[i] = dp[i-1]+1

t = int(input())

for i in range(t):
    quotient = int(input())
    anw = 0
    while quotient > 100:
        remain = quotient % 100
        quotient //= 100
        anw += dp[remain]
    anw += dp[quotient]
    print(anw)
