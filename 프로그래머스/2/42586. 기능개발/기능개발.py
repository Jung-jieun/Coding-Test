def solution(progresses, speeds):
    answer = []
    
    # 작업 시간 계산
    days_remaining = [(100 - p) // s + ((100 - p) % s > 0) for p, s in zip(progresses, speeds)]
    
    # 배포 개수 계산
    while days_remaining:
        deploy_count = 1
        days_to_deploy = days_remaining.pop(0)
        
        # 동시에 배포될 수 있는 작업 개수 확인
        while days_remaining and days_remaining[0] <= days_to_deploy:
            deploy_count += 1
            days_remaining.pop(0)
        
        answer.append(deploy_count)
    
    return answer
