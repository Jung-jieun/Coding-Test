def solution(N, stages):
    answer = []
    level = {}
    num = len(stages)
    
    for n in range(1,N+1):
        if num != 0:
            used = stages.count(n)
            level[n] = used/num
            num -= used
        else:
            level[n] = 0

    return sorted(level, key=lambda x:level[x], reverse=True)