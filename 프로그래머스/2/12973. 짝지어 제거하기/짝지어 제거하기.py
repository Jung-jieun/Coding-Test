from collections import deque
def solution(s):
    s = deque(s)
    q = []
    
    while s:
        char = s.popleft()
        if char not in q:
            q.append(char)
        elif char == q[-1]:
            q.pop()
        else:
            q.append(char)
    
    if len(q)==0:
        return 1
    return 0