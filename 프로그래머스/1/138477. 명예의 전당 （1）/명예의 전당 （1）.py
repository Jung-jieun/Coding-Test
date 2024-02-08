def solution(k, score):
    answer = []
    result = []
    for i in range(len(score)):
        answer.append(score[i])
        if (i+1)<=k:
            result.append(min(answer))
        else:
            answer.sort(reverse=True)
            result.append(answer[k-1])
    return result