def solution(A, B):
    a = list(A)
    n = len(A)
    cnt = 0
    if A == B:
        return 0
    for i in range(n):
        temp = a[-1]
        for j in range(n-1,-1,-1):
            a[j] = a[j-1]
        a[0] = temp
        cnt +=1
        k = ''.join(a)
        if k == B:
            return cnt
    return -1

