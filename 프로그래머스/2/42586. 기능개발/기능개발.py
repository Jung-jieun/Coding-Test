from collections import deque

def solution(progresses, speeds):
    answer = []
    stack = deque()
    
    # 각 기능이 완료되는 데 걸리는 시간을 계산하여 stack에 저장
    for i in range(len(progresses)):
        time = (100 - progresses[i] + speeds[i] - 1) // speeds[i]
        stack.append(time)
    
    # 배포 시점 계산
    while stack:
        # 첫 번째 기능이 완료되는 시간
        function = stack.popleft()
        count = 1
        
        # 같은 시간에 배포될 수 있는 기능들을 체크
        while stack and function >= stack[0]:
            stack.popleft()
            count += 1
        
        # 결과에 추가
        answer.append(count)
    
    return answer
