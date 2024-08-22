def solution(clothes):
    answer = 1
    item = {}
    
    for cloth in clothes:
        if cloth[1] not in item:
            item[cloth[1]] = [cloth[0]]
        else:
            item[cloth[1]].append(cloth[0])
            
    for _, value in item.items():
        answer *= (len(value)+1)
    return answer-1