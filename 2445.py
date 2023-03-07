import math
n=int(input())
for i in range(1,n):
    print("*"*i, end='')
    print(" "*(2*n-2*i), end='')
    print("*"*i)
print("*"*(2*n))
for i in range(1,n):
    print("*"*(n-i), end='')
    print(" "*(2*i), end='')
    print("*"*(n-i))


# for i in range(1, n):
#     print("*"*i)
#     print(" "*())
# 7 5 3 1 0 1 3 5 7