def solution(n, lost, reserve):
    # 모든 학생이 1벌씩 가지고 있다고 가정
    array = [1] * (n+1)
    
    # 여벌의체육복 가져온 학생 
    for r in reserve:
        array[r] += 1
    
    # 도난당한 학생
    for l in lost:
        array[l] -=1
    
    # 체육복 빌려주기
    for i in range(1, n+1):
        if array[i]==0:
        # 앞번호 학생이 여벌의 체육복이 있는 경우
            if (i-1>=1) and (array[i-1]==2): 
                array[i] += 1
                array[i-1] -=1
        # 뒷번호 학생이 여벌의 체육복이 있는 경우 
            elif i+1 <=n and array[i+1]==2: 
                array[i] += 1
                array[i+1] -=1
    
    answer = sum(1 for a in array[1:] if a>0)
    return answer