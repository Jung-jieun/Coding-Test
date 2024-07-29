def solution(new_id):
    answer = ''
    
    # level 1
    new_id = new_id.lower()
    
    # level 2
    for idx in new_id:
        if idx.isalnum() or idx in ('-_.'):
            answer += idx
    
    # level 3
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    # level 4
    if answer[0]=='.' and len(answer)>1:
        answer = answer[1:]
    else:answer
    if answer[-1]=='.':
        answer = answer[:-1]
    else:answer
        
    # level 5
    if answer=='':
        answer += 'a'
    else:
        answer
        
    # level 6
    if len(answer)>=16:
        answer = answer[:15]
        if answer[-1]=='.':
            answer = answer[:14]
    
    # level 7
    if len(answer)<=2:
        answer += answer[-1]*(3-len(answer))
            
    return answer