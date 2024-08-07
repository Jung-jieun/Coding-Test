def solution(survey, choices):
    answer = ''
    # choices : 점수 
    dictionary = {1 : 3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    point = {}
    
    for i in range(len(survey)):
        if choices[i]>4:
            if survey[i][1] not in point:
                point[survey[i][1]] = dictionary[choices[i]]
            if survey[i][0] not in point:
                point[survey[i][0]] = 0
            else:
                point[survey[i][1]] += dictionary[choices[i]]
                point[survey[i][0]] += 0
        
        elif choices[i]<4:
            if survey[i][0] not in point:
                point[survey[i][0]] = dictionary[choices[i]]
            if survey[i][1] not in point:
                point[survey[i][1]] = 0
            else:
                point[survey[i][0]] += dictionary[choices[i]]
        
        elif choices[i]==4:
            if survey[i][0] not in point:
                point[survey[i][0]] = dictionary[choices[i]]
            if survey[i][1] not in point:
                point[survey[i][1]] = dictionary[choices[i]]
            else:
                point[survey[i][0]] += dictionary[choices[i]]
                
    types = 'RTCFJMAN'
    for t in types:
        if t not in point:
            point[t] = 0
                
    if point["R"]>=point["T"]:
        answer += 'R'
    else:
        answer +='T'
    if point['C']>=point['F']:
        answer += 'C'
    else:
        answer += 'F'
    if point['J']>=point['M']:
        answer += 'J'
    else:
        answer += 'M'
    if point['A']>=point['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer