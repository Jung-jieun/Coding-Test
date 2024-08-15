from collections import deque
def solution(n, words):
    passed = []
    words = deque(words)
    idx = 0
    
    while words:
        word = words.popleft()
        passed.append(word)
        idx += 1
        if not words:
            return [0,0]
        else: 
            if passed[-1][-1] != words[0][0] or words[0] in passed:
                time = len(passed)//n+1
                break
    return [idx%n+1, time]