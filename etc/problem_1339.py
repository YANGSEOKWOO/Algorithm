# 날짜비교 알고리즘
def prefer(tod, week, count):
    # 1. 첫번째 년도 비교
    # 2. 달 비교
    # 3. 일 비교
    for i in range(3):
        if tod[0] > week[0]:
            return count
        elif tod[1] > week[1]:
            return count
        elif tod[2] > week[2]:
            return count
        else:
            return 101

terms = ["A 6", "B 12", "C 3"]
today = "2022.05.19"
anw  = []
hak = dict()
for i in terms:
    m, n = i.split(" ")
    hak[m] = int(n)


privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
tod = list(map(int, today.split(".")))
hak_2 = dict()
cnt = 1
for i in privacies:
    # tod = 오늘날짜
    a, b = i.split(" ")
    week = list(map(int, a.split(".")))
    k = week[1] + hak[b]
    week[0] += k//12
    week[1] = k%12
    # week는 term를 반영한 날짜
    ap = prefer(tod,week,cnt)
    if ap != 101:
        anw.append(ap)
    cnt += 1

print(anw)
# dict를 리스트에 넣으면 키 값만 출력이 된다는 사실!!


