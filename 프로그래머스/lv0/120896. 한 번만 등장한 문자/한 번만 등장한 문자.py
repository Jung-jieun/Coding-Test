def solution(s):
    s = list(s)
    num = {}
    for i in s:
        if i not in num:
            num[i]=1
        else:
            num[i] = num[i]+1
    answer = [k for k,v in num.items() if v==1]
    return ''.join(sorted(answer))