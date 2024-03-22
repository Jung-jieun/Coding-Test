import heapq

def solution(scoville, K):
    answer = 0
    h = []
    
    # 모든 원소를 차례대로 힙에 삽입
    for value in scoville:
        heapq.heappush(h, value)
        
    # 가장 작은 두 개의 음식을 섞어서 새로운 음식을 만들고 스코빌 지수를 확인하여 K 이상이 될 때까지 반복
    while h[0] < K:
        if len(h) < 2:
            return -1  # 섞을 음식이 더 이상 없는 경우
        first = heapq.heappop(h)
        second = heapq.heappop(h)
        new_scoville = first + (second * 2)
        heapq.heappush(h, new_scoville)
        answer += 1
        
    return answer

