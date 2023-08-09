def solution(lines):
    num = []
    for line in lines:
        num += line
    start, end = min(num), max(num)
    
    x,y,z = lines
    answer = 0
    
    for i in range(start, end+1):
        result = 0
        
        if x[0] <= i < x[1]:
            result += 1
            
        if y[0] <= i < y[1]:
            result += 1
            
        if z[0] <= i < z[1]:
            result += 1
        
        if result >= 2: 
            answer += 1
    return answer