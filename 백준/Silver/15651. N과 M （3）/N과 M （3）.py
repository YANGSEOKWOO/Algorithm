n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]

def permutations(depth, new_arr, c):
    global arr
    if len(new_arr) == depth:
        print(*new_arr)
        return
    for i in range(len(arr)):
        permutations(depth, new_arr + [arr[i]], i)

permutations(m, [], 0)