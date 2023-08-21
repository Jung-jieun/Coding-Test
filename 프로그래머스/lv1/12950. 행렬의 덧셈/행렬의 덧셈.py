def solution(arr1, arr2):
    result = []
    for i,j in zip(arr1, arr2):
        answer = []
        for a,b in zip(i, j):
            answer.append(a+b)
        result.append(answer)
    return result