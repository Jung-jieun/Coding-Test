def solution(sides):
    sides = sorted(sides)
    if sum(sides[:2])>sides[-1]:
        answer = 1
    else:
        answer = 2
    return answer