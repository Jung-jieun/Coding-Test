def solution(s):
    voca = s.split(' ') # 공백으로 나눴기 때문에
    result = []
    for i in voca:
        answer = ''
        for j in range(0, len(i)):
            if j%2==0 or j==0:
                answer += i[j].upper()
            else: 
                answer += i[j].lower()
        result.append(answer)
    return ' '.join(result) # 공백으로 연결