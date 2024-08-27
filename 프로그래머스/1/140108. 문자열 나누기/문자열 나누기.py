from collections import deque
def solution(s):
    answer = 0
    s = deque(s)
    same = []
    diff = []
    
    while s:
        string = s.popleft()
        same.append(string)
        
        while s:
            if same[-1] == s[0]:
                same.append(s.popleft())
            else:
                diff.append(s.popleft())
                if len(diff)==len(same):
                    answer += 1
                    same = []
                    diff = []
                    break
    if len(same)!=0:
        answer += 1
    return answer