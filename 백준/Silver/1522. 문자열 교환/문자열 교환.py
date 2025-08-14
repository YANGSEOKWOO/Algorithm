s = input()
len_s = len(s)
a = s.count('a')
if a == 0 or a == len_s:
    print(0)
else:
    t = s+s
    b = t[:a].count('b')
    anw = b

    for i in range(1, len_s):
        if t[i-1] == 'b':
            b -=1
        if t[i+a-1] == 'b':
            b +=1
        anw = min(anw, b)

    print(anw)