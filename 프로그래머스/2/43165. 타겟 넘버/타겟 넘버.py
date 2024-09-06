from collections import deque
def solution(numbers, target):
    n = len(numbers)
    answer = 0
    queue = deque()
    queue.append([numbers[0],0])
    queue.append([(-1)*numbers[0],0])
    
    while queue:
        num, idx = queue.popleft()
        idx += 1
        if idx<n:
            queue.append([num+numbers[idx], idx])
            queue.append([num-numbers[idx],idx])
        else:
            if num==target:
                answer += 1
    return answer