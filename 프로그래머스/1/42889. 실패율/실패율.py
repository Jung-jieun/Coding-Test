def solution(N, stages):
    answer = []
    
    num = len(stages)
    
    for level in range(1, N+1):
        challenger = stages.count(level)
        
        if num==0:
            prob = 0
        else:
            prob = challenger/num
        
        answer.append([level, prob])
        num -= challenger
    
    lose_prob = []
    answer.sort(key = lambda x:(-x[1],x[0]))
    
    for i in answer:
        lose_prob.append(i[0])
    return lose_prob