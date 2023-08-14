def solution(n):
    n = str(n)
    return [int(n[i]) for i in range(len(str(n))-1, -1, -1)]

