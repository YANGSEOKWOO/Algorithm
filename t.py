a = [[_]*4 for _ in range(9)]

for row in range(len(a)):
    for col in range(len(a[row])):
        print(a[row][col], end=" ")
    print()

print(a)