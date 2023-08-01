def solution(dots):
    x1, y1 = max(dots)
    x2, y2 = min(dots)
    answer = (x1-x2)*(y1-y2)
    return answer