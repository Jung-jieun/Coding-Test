def solution(before, after):
    before = sorted(before)
    if sorted(after) == before:
        return 1
    return 0