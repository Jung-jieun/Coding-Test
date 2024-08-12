def solution(s):
    answer = ''
    words = s.split(' ')
    
    for i in range(len(words)):
        words[i] = words[i].capitalize()
        
    return ' '.join(words)