def recursion(text,st, ed, cnt):
    if (st >= ed): return 1, cnt
    else:
        if text[st] != text[ed]: return 0, cnt
        else:
            cnt +=1
            return recursion(text, st+1, ed-1, cnt)

n = int(input())
for i in range(n):
    word = input()
    count = 1
    a, b = recursion(word, 0, len(word)-1, count)
    print(a, b)
    
    