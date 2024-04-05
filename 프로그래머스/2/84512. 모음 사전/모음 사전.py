def solution(word):
    dictionary = []
    moum = 'AEIOU'
    
    def recursive(cnt, w):
        if cnt==5:
            return
        for i in range(len(moum)):
            dictionary.append(w + moum[i])
            recursive(cnt+1, w+moum[i])
            
    recursive(0, "")
    
    return dictionary.index(word)+1