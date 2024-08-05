def solution(keymap, targets):
    answer = []
    key_dict = {}
    
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            char = keymap[i][j]
            if char not in key_dict:
                key_dict[char] = j+1 
            else:
                key_dict[char] = min(key_dict[char], (j+1))
                
    for target in targets:
        idx = 0
        for t in target:
            if t in key_dict:
                idx += key_dict[t]
            else:
                idx = -1
                break
        answer.append(idx)
    return answer