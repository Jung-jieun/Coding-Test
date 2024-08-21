def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        y, x = i//n, i%n
        
        value = max(y,x)+1
        
        answer.append(value)
    
    return answer