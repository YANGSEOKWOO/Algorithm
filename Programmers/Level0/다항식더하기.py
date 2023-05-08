def solution(polynomial):
    a = polynomial.split(" + ")
    x_cnt = 0
    cnt = 0
    for i in a:
        if i[-1] == "x":
            if len(i)  == 1:
                x_cnt +=1
            else:
                x_cnt += int(i[:-1])
        else:
            cnt += int(i)
    if x_cnt == 0 and cnt == 0:
        return 0
    elif x_cnt == 0:
        answer = str(cnt)
    elif cnt == 0:
        if x_cnt == 1:
            answer = "x"
        else:    
            answer = str(x_cnt)+"x"
    else:
        if x_cnt == 1:
            answer = "x + "+str(cnt)
        else:
            answer = str(x_cnt)+"x + "+str(cnt)
    return answer