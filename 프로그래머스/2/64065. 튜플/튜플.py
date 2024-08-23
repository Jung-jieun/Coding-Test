def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)
    
    for i in s:
        num = i.split(',')
        for n in num:
            if int(n) not in answer:
                answer.append(int(n))
    return answer