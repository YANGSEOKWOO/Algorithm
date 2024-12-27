import sys
input = sys.stdin.readline

a, b = map(int ,input().split())

def gcd(number_1, number_2):
    if number_1 % number_2 == 0:
        return number_2
    return gcd(number_2, number_1%number_2)

def lcm(number_1, number_2):
    return int(number_1 * number_2 / gcd(number_1, number_2))

print(gcd(a,b))
print(lcm(a, b))