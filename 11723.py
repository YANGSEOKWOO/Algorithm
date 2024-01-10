s = set()

def add(x):
    if x in s:
        return
    else:
        s.add(x)

def remove(x):
    if x in s:
        s.discard(x)

def check(x):
    if x in s:
        return True
    else:
        return False

def toggle(x):
    if check(x):
        remove(x)
    else:
        add(x)

def all():
    global s
    s = set(str(i) for i in range(1, 21))

def empty():
    global s
    s = set()

import sys
input = sys.stdin.readline

m = int(input())

for i in range(m):
    word = list(input().split(" "))
    if len(word) == 1:
        if word[0].strip() == 'empty':
            empty()
        elif word[0].strip() == 'all':
            all()
    else:
        if word[0] == 'add':
            add(word[1].strip())
        elif word[0] == 'remove':
            remove(word[1].strip())
        elif word[0] == 'check':
            if check(word[1].strip()):
                print('1')
            else:
                print('0')
        elif word[0].strip() == 'toggle':
            toggle(word[1].strip())



