n = input()

while n != '.':
    stk = []
    check = True
    for i in n:
        if i == '['or i == '(':
            stk.append(i)
        if i == ')':
            if len(stk) == 0 or stk[-1] != '(':
                print('no')
                check = False
                break
            elif stk[-1] == '(':
                stk.pop()
        if i == ']':
            if len(stk) == 0 or stk[-1] != '[':
                print('no')
                check = False
                break
            elif stk[-1] == '[':
                stk.pop()
    if len(stk) == 0 and check:
        print('yes')
    elif len(stk) != 0 and check:
        print('no')
    n = input()
        
            