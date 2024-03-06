def solution(citations):
    answer = []
    h_index = [i for i in range(1,len(citations)+1)]
    citations.sort(reverse=True)
    for h, p in zip(h_index, citations):
        if h<p:
            answer.append(h)
        else:
            answer.append(p)
    return max(answer)