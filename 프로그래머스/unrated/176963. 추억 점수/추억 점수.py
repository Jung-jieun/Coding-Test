def solution(name, yearning, photo):
    result = []
    for i in photo:
        answer = []
        for j in range(len(name)):
            if name[j] in i:
                answer.append(yearning[j])
        result.append(sum(answer))
    return result