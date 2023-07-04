def solution(numer1, denom1, numer2, denom2):
    denom = denom1*denom2 # 분모
    num = numer1*denom2 + numer2*denom1 # 분자
    for i in reversed(range(1, min(denom, num)+1)):
        if denom%i ==0 and num%i ==0:
            num, denom = num//i, denom//i
    return [num, denom]
    