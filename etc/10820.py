

while True:
    try:
        word = input()
        lower = 0
        upper = 0
        num = 0
        blank = 0
        for i in word:
            if 97<= ord(i) <= 122:
                lower += 1
            elif 65<= ord(i) <= 90:
                upper += 1
            elif i == " ":
                blank += 1
            elif 48 <= ord(i) <= 57:
                num += 1
        print(lower, upper, num, blank)
    except EOFError:
        break
