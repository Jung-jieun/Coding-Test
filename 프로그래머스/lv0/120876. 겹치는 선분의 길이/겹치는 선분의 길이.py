def solution(lines):
    sets = [set(range(min(line), max(line))) for line in lines]
    return len(sets[0]&sets[1] | sets[0]&sets[2] | sets[1]&sets[2])