"""

5 3
1 1000

2 7000

0 6000
1 2000
2 7000

15000

"""

n, k = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda x:-x[1])

while k:
    lst2 = lst[:k]
    lst.sort()   

