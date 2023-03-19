n , k = map(int, input().split())
# [무게, 가치]
thing = [[0,0]]
# k : 무게
dn = [[0]*(k+1) for _ in range(n+1)]
# 
for _ in range(n):
    thing.append(list(map(int, input().split())))
# i : 배낭에 들어갈 물건 1개
# j 
for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]
        # 무게 저장이 안됨
        if j < w:
            dn[i][j] = dn[i-1][j] # 그 전에 있던 걸 그대로 가져온다.
        else:
            # 만약 이번의 i를 넣었을 때 값이 더 크다면 
            dn[i][j] = max(dn[i-1][j-w]+v, dn[i-1][j])
# dn[i][j] 란 물품수가 i개, 무게가 j인 경우의 최대값을 넣는것
print(dn[n][k])