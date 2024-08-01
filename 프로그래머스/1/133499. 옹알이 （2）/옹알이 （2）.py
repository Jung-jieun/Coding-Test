def solution(babbling):
    answer = 0
    
    string = ["aya", "ye", "woo", "ma"]
    
    for i in range(len(babbling)):
        for s in string:
            if s*2 not in babbling[i]:
                babbling[i] = babbling[i].replace(s, ' ')
        
        if babbling[i].isspace():
            answer += 1
    
    return answer