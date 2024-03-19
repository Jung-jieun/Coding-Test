def solution(participant, completion):
    name_part = dict.fromkeys(set(participant), 0)
    for name in participant:
        name_part[name] += 1
        
    for name in completion:
        name_part[name] -= 1
        
    for name, count in name_part.items():
        if count>0:
            return name

