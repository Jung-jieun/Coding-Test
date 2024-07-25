def solution(word):
    word_list = []
    moeum = "AEIOU"
    def dfs(length, alpha):
        # 종료시점
        if length==5:
            return
        
        for i in range(len(moeum)):
            word_list.append(alpha+moeum[i])
            dfs(length+1, alpha+moeum[i])
            
    dfs(0, "")
    return word_list.index(word)+1