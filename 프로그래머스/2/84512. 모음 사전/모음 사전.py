def solution(word):
    answer = 0
    string = 'AEIOU'
    dictionary = []
    
    def dfs(cnt, w):
        if cnt==5:
            return 
        
        for s in string:
            dictionary.append(w+s)
            dfs(cnt+1, w+s)
    
    dfs(0, '')
    return dictionary.index(word)+1