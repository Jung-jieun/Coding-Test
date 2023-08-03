def solution(sides):
    sides.sort()
    answer = []

    for i in range(1,sides[0]+sides[1]):    
        
        # 나머지 한 변이 가장 긴 변일 때
        if i >= sides[1]: 
            answer.append(i)
            
    for j in range(1, sides[1]):       
        # 가장 긴 변이 존재할 때
        if sides[0] + j > sides[1]:
            answer.append(j)
            
    
    return len(answer)