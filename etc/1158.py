n, k = map(int, input().split())
arr = [ i for i in range(1,n+1)]
print(arr)
ptr = k-1
anw = []
for i in range(n):
    if ptr > len(arr):
        ptr = ptr%len(arr)
        anw.append(str(arr.pop(ptr)))
        ptr += k-1
    else:
        anw.append(str(arr.pop(ptr)))
        ptr += k-1
print("<",", ".join(anw)[:],">", sep='')
# < 1, 2, 3, 4, 5, 6, 7>

# < 3, 6, 