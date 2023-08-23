def solution(n):
    answer = []
    while n>=1:
        answer.append(n%3)
        n = n//3
    num = ''.join(str(i) for i in answer)
    return int(num, 3)