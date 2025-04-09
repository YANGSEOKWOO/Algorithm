# 자연수 n, m을 가진다.
n, m = map(int, input().split())

'''
중복 없이 N개 중 중복없이 M개를 고른 수열
=> nPm
'''

arr = [i for i in range(1, n+1)]
visited = [0]*n
def permutations(n, new_arr):
    global arr
    if len(new_arr) == n:
        print(*new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            permutations(n, new_arr+ [arr[i]])
            visited[i] = 0

permutations(m, [])