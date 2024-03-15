import heapq as hp
def solution(scoville, K):
    answer = 0
    hp.heapify(scoville)
    
    if scoville[0]>K:
        return answer
    
    while scoville[0] < K:
        if len(scoville)==1:
            return -1
        first = hp.heappop(scoville)
        second = hp.heappop(scoville)
        
        hp.heappush(scoville, first+second*2)
        answer += 1
    return answer