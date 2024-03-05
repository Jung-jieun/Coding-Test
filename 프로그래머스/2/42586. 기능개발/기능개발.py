def solution(progresses, speeds):
    answer = []
    
    while progresses: #비어 있으면 끝
        cnt = 0 # 배포 수
        
        while progresses and progresses[0]>=100: 
            # 리스트가 남아있고 맨 앞에 작업진도가 100이 된다면
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
        
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        # progresses update.
        
        # 만약 오늘 배포된 기능 개수가 0이 아니라면 결과 리스트에 추가.
        if cnt:
            answer.append(cnt)
    return answer