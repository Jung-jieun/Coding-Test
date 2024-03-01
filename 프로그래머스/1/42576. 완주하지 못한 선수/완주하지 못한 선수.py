def solution(participant, completion):
    hashdict = {}
    sumhash = 0
    
    #1. hash : participant의 dictionary 만들기
    for part in participant:
        hashdict[hash(part)] = part # participant 이름
        #2. participant의 sum(hash) 구하기
        sumhash += hash(part) # hash한 값
        
    #3. completion의 sum(hash) 빼기
    for comp in completion:
        sumhash -= hash(comp)
        
    #4. 남은 값이 완주하지 못한 선수의 hash 값
    return hashdict[sumhash]