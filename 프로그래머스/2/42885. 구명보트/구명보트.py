def solution(people, limit):
    answer = 0
    
    if sum(people) < limit:
        return 1
    
    people.sort()
    
    i, j = 0, len(people)-1
    
    while i<=j:
        if people[i]+people[j]>limit:
            j -= 1
            answer += 1
        else:
            answer += 1
            i += 1
            j -= 1
        
    return answer