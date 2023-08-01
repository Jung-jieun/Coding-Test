def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    answer = array.index(height)
    return answer