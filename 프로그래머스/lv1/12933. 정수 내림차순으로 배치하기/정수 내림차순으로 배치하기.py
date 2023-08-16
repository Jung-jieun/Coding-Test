def solution(n):
    n = str(n)
    num = sorted([n[i] for i in range(0, len(n))], reverse=True)
    return int(''.join(num))