def solution(a, b, n):
    answer = 0
    coke = n
    while coke>=a:
        eaten = coke//a*b
        answer += eaten
        coke = coke%a + eaten
    return answer