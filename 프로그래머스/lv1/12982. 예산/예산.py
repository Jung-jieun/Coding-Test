def solution(d, budget):
    d = sorted(d)
    result = 0
    for i in range(len(d), 0, -1):
        if sum(d[:i])<=budget:
            result += 1
    return result