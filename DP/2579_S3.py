import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*(n+1)
stair = [0]
for i in range(n):
    stair.append(int(input()))
if n == 1:
    print(stair[1])
elif n == 2:
    print(stair[1]+ stair[2])
else:
    dp[1] = stair[1]
    dp[2] = stair[2]+ stair[1]
    for i in range(3, n+1):
        dp[i] = max( dp[i-3]+stair[i]+stair[i-1], dp[i-2]+stair[i])
    print(dp[n])
# for i in range(1,len(stair)):
    