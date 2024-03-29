def solution(n, lost, reserve):
    
    # 여벌 체육복을 가져왔는데 도난 당한 경우 제외 -> reserve랑 lost랑 중복 없애기
    two = [r for r in reserve if r not in lost]
    
    # 체육복을 빌릴 수 있는 학생들 -> reserve랑 lost 중복 없애기
    rent = [l for l in lost if l not in reserve]
    
    two.sort()
    rent.sort()
    
    for idx in two:
        if idx-1 in rent:
            rent.remove(idx-1)
        elif idx+1 in rent:
            rent.remove(idx+1)
    
    return n-len(rent)