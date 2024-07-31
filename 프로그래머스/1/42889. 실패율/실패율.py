def solution(N, stages):
    result = {}
    user = len(stages)
    for level in range(1, N+1):
        if user != 0:
            count = stages.count(level)
            result[level] = count/user
            user -= count
        else:
            result[level] = 0
    return sorted(result, key = lambda x:result[x], reverse=True)