from collections import deque
def solution(progresses, speeds):
    answer = []
    q = deque()
    num = 0
    
    for i, j in zip(progresses, speeds):
        if (100-i)%j==0:
            q.append((100-i)//j)
        else:
            q.append((100-i)//j+1)
    
    while q:
        work = q.popleft()
        num += 1
        while q and work>=q[0]:
            num += 1
            q.popleft()
        answer.append(num)
        num = 0
    return answer