def solution(left, right):
    num = 0
    answer = []
    for i in range(left, right+1):
        if (i**0.5).is_integer()==False:
            answer.append(i)
        else:
            answer.append(-1*i)     
    return sum(answer)