from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        time = 0
        price = prices.popleft()
        for p in prices:
            if price > p:
                time += 1
                break
            time += 1
        answer.append(time)
    
    return answer