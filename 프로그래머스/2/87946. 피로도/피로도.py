from itertools import permutations
def solution(k, dungeons):
    answer = -1
    
    
    for p in permutations(dungeons, len(dungeons)):
        cnt = 0
        tmp = k
        
        for need, spend in p:
            if tmp>=need:
                tmp -= spend
                cnt += 1
        answer = max(answer, cnt)
    return answer