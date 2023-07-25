def solution(array, n):
    answer = []
    array.sort()
    for i in array:
        answer.append((abs(n-i)))
    result = [array[answer.index(min(answer))]]
    result = sorted(result)
    if len(result)>1:
        return min(result)
    else:
        return result[0]