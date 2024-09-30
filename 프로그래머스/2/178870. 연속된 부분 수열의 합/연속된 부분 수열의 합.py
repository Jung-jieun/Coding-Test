def solution(sequence, k):
    dic = {idx:num for idx, num in enumerate(sequence)}
    start = last = 0
    answer = []
    
    for idx, num in enumerate(sequence):
        end = idx
        last += num
        while last>k:
            last -= dic[start]
            start += 1
        if last==k:
            answer.append([start, end])
    answer.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answer[0]