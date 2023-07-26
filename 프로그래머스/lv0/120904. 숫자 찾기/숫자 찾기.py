def solution(num, k):
    answer = []
    for i in str(num):
        answer.append(int(i))
    if k in answer:
        return answer.index(k)+1
    else:
        return -1