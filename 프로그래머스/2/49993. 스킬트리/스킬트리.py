def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        exist = ''
        not_exist = ''
        
        for t in tree:
            if t not in skill:
                not_exist += t
            else:
                exist += t
        
        length = len(exist)
        if exist==skill[:length]:
            answer += 1
        elif len(exist)==0 and not_exist:
            answer += 1
    
    return answer