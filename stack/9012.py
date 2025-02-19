n = int(input())


def vps_test(word):
    stack = []
    for i in word:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
    
for i in range(n):
    vps = input()
    if vps_test(vps):
        print("YES")
    else:
        print("NO")

