def solution(common):
    if common[1]-common[0] == common[-1]-common[-2]:
        answer = (common[1]-common[0])+common[-1]
    else:
        answer = (common[-1]//common[-2])*common[-1]
    return answer