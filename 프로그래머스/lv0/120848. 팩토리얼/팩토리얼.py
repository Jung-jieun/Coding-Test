def solution(n):
    i = 1
    answer =1
    while (n>=answer):
        i += 1
        answer =answer * i
    return i-1