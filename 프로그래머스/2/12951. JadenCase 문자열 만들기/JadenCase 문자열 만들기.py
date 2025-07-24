def solution(s):
    answer = ''
    flag = True
    
    for i in range(len(s)):
        # 첫번째 일 때
        if s[i] != " " and flag:
            if 97 <= ord(s[i]) <= 122:
                answer += chr(ord(s[i]) - 32)  # ord(s[i]) - 32
            else:
                answer += s[i]
            flag = False
        elif s[i] == " ":
            answer += s[i]
            flag = True
        else:
            if 65 <= ord(s[i]) <= 90:
                answer += chr(ord(s[i]) + 32)  # ord(s[i]) + 32
            else:
                answer += s[i]
        
    return answer