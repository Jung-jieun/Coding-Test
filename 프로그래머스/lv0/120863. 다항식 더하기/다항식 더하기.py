def solution(polynomial):
    answer = polynomial.split(' + ')
    coef = 0
    const = 0
    for i in answer:
        if i == "x":
            coef += 1
        elif "x" in i:
            coef += int(i[:-1])
        else:
            const += int(i)
    if coef != 0: #계수가 0이 아닐 때
        if coef ==1: # 계수가 1일 때
            if const != 0: # 상수가 0이 아닐 때
                answer = f'x + {const}'
            else: # 상수가 0일 때
                answer = f'x'
        else: # 계수가 1이 아닐 때
            if const !=0: # 상수가 0이 아닐 때
                answer = f'{coef}x + {const}'
            else: # 상수가 0일 때
                answer = f'{coef}x'
    else:  # 계수가 0일 때 
        if const !=0: # 상수가 0이 아닐 때
            answer = f'{const}'
    return answer
