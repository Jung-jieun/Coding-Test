def solution(array, commands):
    answer = []
    for com in commands:
        i = com[0]
        j = com[1]
        k = com[2]
        num = array[i-1:j]
        num.sort()
        answer.append(num[k-1])
    return answer