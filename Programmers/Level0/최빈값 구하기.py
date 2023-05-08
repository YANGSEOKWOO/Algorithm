def solution(array):
    anw = []
    n = len(array)
    map = [0]*(1001)
    for i in range(n):
        map[array[i]] += 1
    max_cnt = max(map)
    for i in range(1001):
        if map[i] == max_cnt:
            anw.append(i)
    if len(anw) == 1:
        return anw[0]
    return -1
    