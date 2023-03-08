import sys
input = sys.stdin.readline

n = int(input())
anw = ''
if n == 0:
    print(0)
else:
    while n!= 0:
        if n%(-2):
            anw = '1' + anw
            n = n//-2 +1
        else:     
            anw = '0' + anw
            n //= -2
    print(anw)

