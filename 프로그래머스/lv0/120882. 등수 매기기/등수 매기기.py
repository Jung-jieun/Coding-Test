def solution(score):
    answer = []
    rank = []
    for i in score:
        answer.append((i[0]+i[1])/2)
        
    for j in answer:
        rank.append(sorted(answer, reverse=True).index(j)+1)
    return rank