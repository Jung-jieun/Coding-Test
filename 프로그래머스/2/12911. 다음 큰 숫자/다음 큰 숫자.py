def solution(n):
    answer = n+1
    
    while True:
        var1 = bin(answer)[2:] 
        var2 = bin(n)[2:]
        
        if var1.count("1") == var2.count("1"):
            break
        else:
            answer += 1
        
    return answer