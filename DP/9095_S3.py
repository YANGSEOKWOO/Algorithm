def sol(n):
    if n ==1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return sol(n-1)+ sol(n-2) + sol(n-3)

t = int(input())
for _ in range(t):
    n = int(input())
    print(sol(n))
# n : 1,5,2,3,4,6,7,8,9,10

