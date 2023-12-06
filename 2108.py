import sys
input = sys.stdin.readline

n = int(input())
number = [int(input()) for _ in range(n)]
number.sort()
print(int(round(sum(number)/n,0)))
# print('number', number)
print(number[n//2])

current_number = 0
current_freq = 0
max_number = 0
max_freq = 0
isChanged = False
for i in number:
    if i == current_number:
        current_freq+=1
    else:
        current_freq = 1
        current_number = i
    if current_freq == max_freq:
        if not isChanged:
            max_number = i
            max_freq = current_freq
            isChanged = True
    elif current_freq > max_freq:
        max_number = i
        max_freq = current_freq
        isChanged = False
print(max_number)

print(number[-1]-number[0])