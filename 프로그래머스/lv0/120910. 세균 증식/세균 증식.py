def solution(n, t):
    answer = 0
    for i in range(1,t+1):
        answer = n*2
        n += n
    return answer