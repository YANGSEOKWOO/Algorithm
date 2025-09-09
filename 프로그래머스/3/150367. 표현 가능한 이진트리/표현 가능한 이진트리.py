def solution(numbers):
    answer = []
    
    for number in numbers:
        bin_number = str(bin(number))[2:]
        len_bin_number = len(bin_number)
        purpose_len=0
    
        def check_length(len_bin_number):
            while True:
                if (len_bin_number-1)%2==0:  
                    len_bin_number = (len_bin_number-1)/2
                    if len_bin_number==0:
                        return True
                else:
                    return False 
                        
        ck_len=check_length(len_bin_number)
        if ck_len:
            tmp=0
            while True:
                purpose_len = purpose_len+2**tmp
                if purpose_len==len_bin_number:
                    break
                tmp+=1
        
            isValid=True
            for i in range(1,tmp+1):
                if not isValid:
                    break
                k= 2**i
                plus= k*2
                index=0
                while isValid:
                    if k+plus*index-1> len(bin_number)-1:
                        break
                    if bin_number[k+plus*index-1] == "0":
                        if bin_number[k+plus*index-1-(2**(i-1))] =="1"  or bin_number[k+plus*index-1+(2**(i-1))] == "1":
                            isValid = False 
                            break
                    index+=1

            if isValid:
                answer.append(1)
            else:
                answer.append(0)
            
                
                
        else:
            tmp=0

            while True:
                purpose_len = purpose_len+2**tmp
                if purpose_len>len_bin_number:
                    break
                tmp+=1
        
            zero=""
            for i in range(purpose_len -len_bin_number):
                zero+="0"
            
            bin_number = zero+bin_number
            
            isValid=True
            for i in range(1,tmp+1):
                if not isValid:
                    break
                k= 2**i
                plus= k*2
                index=0
                while isValid:
                    if k+plus*index-1> len(bin_number)-1:
                        break
                    if bin_number[k+plus*index-1] == "0":
                        print()
                        if bin_number[k+plus*index-1-(2**(i-1))] =="1"  or bin_number[k+plus*index-1+(2**(i-1))] == "1":
                            isValid = False 
                            break
                    index+=1
                            
            if isValid:
                answer.append(1)
            else:
                answer.append(0)


    return answer
                    
#                         16
                    
# #           8                             
# #     4          12             20  
# #  2    6     10     14      18      22
# # 1 3  5  7  9  11 13  15  17  19  21  23 
                    


## 일단  포화 이진트리 이므로 1-> 3->7... 이 순서대로 길이는 정해져있음
## 만약 순서가 같다면 바로 따지면 됨
## 그리고 순서가 다르다면 0을 넣어서 길이를 맞추면 됨 이때 0을 어디에 넣을지가 관건


## 여기서 중요한 점은 마지막 노드들 즉 높이가 가장 큰 부분에서만 0을 넣을 수 있다는 것임
## 그위에는 0이 될 수 있는경우는 아래도 다 0이여야함 즉 위에 노드에서 0이면 아래도 00 이여야한다는것
## 그렇다면 루트를 기준으로 마지막 노드가 아닌경우 0이 나온다면 나머지는 무조건 0이여야함 
# 0001101


# 2**50

# 50줄

# 1->3->7->15->31->63
# 최대 6줄
# 1 ≤ numbers의 길이 ≤ 10,000
# 1 ≤ numbers의 원소 ≤ 10**15

# DFS로 풀면..? 
## 0을 32개 넣는다고 가정 

## 1,0,1,0,1,0,1,0,1,0,1,0,1,0,1
## 결국 보면 짝수에 0이 들어가면 안됨 .

## 그리고 값이 변경이 안될려면 맨앞에만 0이 가능한거 같은디 
