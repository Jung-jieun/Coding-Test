def solution(genres, plays):
    answer = []
    dic1 = {}
    dic2 = {}
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre in dic1:
            dic1[genre].append((idx, play))
        else:
            dic1[genre] = [(idx, play)]
            
        if genre in dic2:
            dic2[genre] += play
        else:
            dic2[genre] = play
    
    for (kind, volume) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (idx, play) in sorted(dic1[kind], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(idx)
    
    return answer