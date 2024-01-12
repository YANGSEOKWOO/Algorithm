a_1, a_0 = map(int, input().split(" "))
c = int(input())
n = int(input())

if (a_1*n + a_0) <= c*n and a_1 <= c:
    print('1')
else:
    print('0')