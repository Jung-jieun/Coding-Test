def solution(name, yearning, photo):
    answer = []
    scores = {}
    result = 0
    
    for i, j in zip(name, yearning):
        scores[i] = j
        
    for photos in photo:
        result = 0
        for p in range(len(photos)):
            for k, score in scores.items():
                if k==photos[p]:
                    result += score
        answer.append(result)
    return answer