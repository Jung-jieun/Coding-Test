def solution(number, limit, power):
    num = [i for i in range(1, number+1)]
    result = []
    
    for j in num:
        answer = 0
        for k in range(1, int(j**(1/2))+1):
            if j%k==0:
                answer += 1
                if (k**2) != j : 
                    answer += 1
        if answer>limit:
            result.append(power)
        else:
            result.append(answer)
        
    return sum(result)