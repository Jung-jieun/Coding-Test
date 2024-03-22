import heapq
def solution(scoville, K):
    answer = 0
    h = []
    
    for value in scoville:
        heapq.heappush(h, value)
        
    while h[0]<K:
        
        if len(h)<2:
            return -1
        
        first = heapq.heappop(h)
        second = heapq.heappop(h)
        new = first + (second*2)
        heapq.heappush(h, new)
        answer += 1
    return answer