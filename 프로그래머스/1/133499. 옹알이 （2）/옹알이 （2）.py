def solution(babbling):
    answer = 0
    string = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        for i in string:
            if i*2 not in word:
                word = word.replace(i, " ")
        
        if word.isspace():
            answer += 1
    
    return answer