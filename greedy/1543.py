# 사고과정, 접근법 기록
'''
일단 자체는 되게 간단해 보였음
찾으면 삭제하고, 다시 찾으면 삭제하면 되니까
'''
string = input()
finder = input()

def findString(text, search_text):
    start_index = 0
    cnt = 0

    while True:
        found_index = text.find(search_text, start_index)

        if found_index == -1:
            break

        cnt +=1
        start_index = found_index+ len(search_text)
    return cnt
print(findString(string, finder))
