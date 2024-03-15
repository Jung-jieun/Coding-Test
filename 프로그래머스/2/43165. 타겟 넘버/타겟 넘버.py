def solution(numbers, target):
    answer = 0
    q = [[0,0]]
    
    while len(q)>0:
        idx, n = q.pop()
        
        if idx < len(numbers):
            q.append([idx+1, n + numbers[idx]])
            q.append([idx+1, n - numbers[idx]])
            
        if idx == len(numbers) and n == target:
                answer +=1
    
    return answer