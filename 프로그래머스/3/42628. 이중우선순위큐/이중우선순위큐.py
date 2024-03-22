import heapq
def solution(operations):
    answer = []
    
    for ope in operations:
        if "I" in ope:
            heapq.heappush(answer, int(ope[2:]))
        elif ope=="D -1":
            if answer:
                heapq.heappop(answer)
        elif ope=="D 1":
            if answer:
                answer.pop(answer.index(max(answer)))
    
    if len(answer)==0:
        return [0,0]
    else:
        return [max(answer), min(answer)]