from itertools import permutations
def solution(clothes):
    answer = 1
    wear = {}
    
    for item in clothes:
        kind = item[1]
        
        if kind in wear:
            wear[kind] += 1
        else:
            wear[kind] = 1
    
    for kind, count in wear.items():
        answer *= (count+1)
    
    return answer-1