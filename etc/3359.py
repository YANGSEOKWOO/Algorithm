import sys
import math
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)

s, l = map(int, input().split())
dp[1] = l+s
temp_right = s
for i in range(2,n+1):
    s, l = map(int, input().split())
    if (l +s + abs(l-temp_right)) >  (l +s + abs(s-temp_right)): # 길이가 작은 게 위쪽일때
        dp[i] = dp[i-1] + l +s + abs(l-temp_right) - temp_right
        temp_right = l
    else:
        dp[i] = dp[i-1] + l + s + abs(s-temp_right) - temp_right
        temp_right = s

print(dp[n])