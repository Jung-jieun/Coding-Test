def solution(array, commands):
    result = []
    answer = []
    num = []
    for i in commands:
        result.append(sorted(array[i[0]-1:i[1]]))
        num.append(i[2])
    for j, k in enumerate(num):
        answer.append(result[j][k-1])
    return answer