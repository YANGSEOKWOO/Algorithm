from time import time
import modul as cal
word = ["몬스터 주식회사", "강아지가 뛰어간다", "메리크리스마스", "코난", "16강 진출"]
a = 3
b = 2
print(cal.add(3,2))
while(1):
    print("어떤것을 진행?")
    print("1. 타자게임 2. 단어추가 3. 단어장 출력 4. 프로그램 종료")

    game = input()

    if game == "1":
        start_time = time()
        #타자 게임
        game_count = 0
        while game_count < len(word):
            print(word[game_count])
            user_input = input()
            if(word[game_count] == user_input):
                print("통과")
                game_count +=1
            elif(word[game_count] != user_input):
                print("오타! 다시 도전!")
        finish_time = time()
        print("타자 시간 : ", round(finish_time-start_time,2))

    elif game =="2":

        print("단어장에 어떤 데이터를 추가 할까요?")
        new_word = input()
        word.append(new_word)
        print("단어장에", new_word, "추가완료!")
    elif game == "3":
        print(word)
    elif game == "4":
        print("프로그램을 종료합니다")
    break

