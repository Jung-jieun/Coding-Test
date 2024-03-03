def solution(genres, plays):
    answer = []
    
    dic1 = {} # genre, index, play 저장
    dic2 = {} # genre별 총 play 수
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic1:
            dic1[genre] = [(idx, play)] # index와 play수를 함께 저장
        else:
            dic1[genre].append((idx, play))
        
        if genre not in dic2:
            dic2[genre] = play
        else:
            dic2[genre] += play    
        
    for (kind, volume) in sorted(dic2.items(), key=lambda x:x[1], reverse=True): # dic2 정렬
        for (idx, play) in sorted(dic1[kind], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(idx)
    return answer