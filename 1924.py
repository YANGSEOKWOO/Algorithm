date = [0,31,28,31,30,31,30,31,31,30,31,30,31]

mon, day = map(int, input().split())
total = sum(date[:mon])+day
cal = total%7
if cal == 1:
    print('MON')
elif cal == 2:
    print('TUE')
elif cal == 3:
    print("WED")
elif cal == 4:
    print("THU")
elif cal == 5:
    print("FRI")
elif cal == 6:
    print("SAT")
else:
    print("SUN")