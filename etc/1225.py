import sys
input = sys.stdin.readline 
a, b = map(int, input().split())

list_a = list(str(a))
list_b = list(str(b))

anw = 0
for i in list_a:
    num_1 = int(i)
    for j in list_b:
        num_2 = int(j)
        anw += num_1 * num_2
print(anw)

