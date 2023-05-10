def solution(numbers):
    sorted_num = sorted(numbers, reverse=True)
    answer = sorted_num[0]*sorted_num[1]
    return answer