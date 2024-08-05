from collections import deque
def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    q = deque(s)
    while q:
        word = q.popleft()
        idx = alpha.index(word)
        count = 0
        
        while count<index:
            idx = (idx+1) % 26
            if alpha[idx] not in skip:
                count += 1
        answer += alpha[idx]
    return answer