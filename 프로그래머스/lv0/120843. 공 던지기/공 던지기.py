def solution(numbers, k):
    answer = numbers*k
    result = list(answer[0::2])
    return result[k-1]