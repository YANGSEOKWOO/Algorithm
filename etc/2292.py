def floor(number):
    temp = (number-1)/3
    return int(temp ** 0.5 + 0.5) +1

n = int(input())
print(floor(n))
