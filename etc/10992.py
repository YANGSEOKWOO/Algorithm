n = int(input())
# n-1 ~ 0
for i in range(n):
    print(" "*(n-i-1), end='')
    if i == 0:    
        print("*")
    elif i == n-1:
        print("*"*(2*n-1))
    else:
        print("*", end='')
        print(" "*(2*i-1), end='')
        print("*")