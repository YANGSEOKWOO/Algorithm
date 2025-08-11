n,m,t,k = map(int,input().split())


lst=[]


res_point=[]
res=0
for i in range(t):
    a ,b = map(int,input().split())
    lst.append((a,b))



for i in lst:
    for j in lst:
        x1 = max(0, min(i[0], n - k))
        y1 = max(0, min(j[1], m - k))

        tmp = 0
        for tx, ty in lst:
            if x1 <= tx <= x1 + k and y1 <= ty <= y1 + k:
                tmp += 1

        if tmp > res:
            res = tmp
            res_point = [x1, y1 + k]

print(res_point[0], res_point[1])
print(res)

    

