def solution(s, n):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    s_low = s.lower()
    num = []
    for i in range(0, len(s_low)):
        num.append(alpha.find(s_low[i]))
    num2 = [j+n if j!=-1 else -1 for j in num ]
    for k in num2:
        if k>=26:
            num2[num2.index(k)] = k%26
    result = []
    for a in num2:
        if a!=-1:
            result.append(alpha[a])
        else:
            result.append(-1)
    answer = ''
    for i in range(len(s)):
        if s[i].islower()==True:
            answer+=result[i]
        else:
            if result[i]==-1:
                answer+=' '
            else:
                result[i] = result[i].upper()
                answer+= result[i]
    return answer