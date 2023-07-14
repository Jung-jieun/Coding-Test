def solution(numbers, direction):
    answer = []
    if direction=="right":
        answer = numbers[0:len(numbers)-1]
        answer.insert(0, numbers[-1])
    else:
        answer = numbers[1:len(numbers)]
        answer.append(numbers[0])
    return answer
            