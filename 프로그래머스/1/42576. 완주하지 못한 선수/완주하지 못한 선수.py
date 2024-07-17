def solution(participant, completion):
    name = {}
    for i in participant:
        if i not in name:
            name[i] = 1
        else:
            name[i] += 1
    for j in completion:
        if name[j]>=1:
            name[j]-=1
    
    not_com = [key for key, value in name.items() if value==1]
    
    return not_com[0]
        