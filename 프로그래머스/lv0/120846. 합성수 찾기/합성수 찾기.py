def division(n):
    result = 0
    for i in range(1, n+1):
        if n%i==0:
            result += 1
    return result

def solution(k):
    answer = 0
    for n in range(1, k+1):
        if division(n)>2:
            answer +=1
    return answer

    
            
                