def solution(k, tangerine):
    answer = 0
    types = {}
    result = 0
    
    for t in tangerine:
        if t not in types:
            types[t] = 1
        else:
            types[t] += 1
    types = sorted(types.items(), key = lambda x:x[1], reverse=True)
    
    for i in range(len(types)):
        if answer<k:
            answer += types[i][1]
        else:
            break
        result = i+1
    
    return result
    