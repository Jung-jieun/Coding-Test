def solution(s):
    answer = []
    result = list(s.split())
    for i in result:
        answer.append(int(i))
    answer.sort()

    return  "{0} {1}".format(min(answer), max(answer))