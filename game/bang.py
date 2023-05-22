import sys

a, b = map(int, sys.stdin.readline().split())
a_card = list(map(int, sys.stdin.readline().split()))
b_card = list(map(int, sys.stdin.readline().split()))



def anw(a_card, b_card):
    check = ''.join(map(str,a_card))
    k =  min(len(a_card), len(b_card))
    anw = 0

    a_card_str= ''.join(map(str,a_card)).rstrip('\n')
    
    for i in range(k,1,-1):
        # print("i= " , i)
        for j in range(len(b_card)-i+1):
            new = ''.join(map(str,b_card[j:i+j])).rstrip('\n')
            tp = -1
            flag = True
            for ti in range(len(new)):
                temp = a_card_str.find(new[ti])
                if temp == -1 or tp> temp:
                    flag = False
                    break
                else:
                    tp = temp
            if flag:
                return i
    return anw

anwswer = anw(a_card, b_card)
print(anwswer)