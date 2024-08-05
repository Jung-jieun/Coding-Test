from collections import deque
def solution(s):
    answer = 0
    q = deque(s)
    
    while q:
        x = q.popleft()
        a = 1
        b = 0
        while q:
            n = q.popleft()
            if x==n:
                a += 1
            else:
                b += 1
                
            if a==b:
                answer += 1
                break
        if a!=b:
            answer += 1
    return answer