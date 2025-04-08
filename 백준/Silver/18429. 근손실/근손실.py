n, k = map(int, input().split())
dumbel = list(map(int, input().split()))
visited = [False]*n

result = 0
def backtracking(weight, N):
    global n
    global result
    global k
    if weight < 500:
        return
    if N == n:
        result += 1
        return
    weight -= k
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            backtracking(weight + dumbel[i], N+1)
            visited[i] = False

backtracking(500, 0)
print(result)