def solution(babbling):
    talk = [ "aya", "ye", "woo", "ma"]
    answer = 0
    for i in babbling:
        for j in talk:
            i = i.replace(j, ' ')
        i = i.replace(' ', '')
        if len(i)==0:
            answer+=1
    return answer