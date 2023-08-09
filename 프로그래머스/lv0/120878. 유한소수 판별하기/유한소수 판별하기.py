def solution(a, b):
    # 기약분수 만들기 
    answer = []
    i = 2
    while i<=b:
        if b%i==0 and a%i==0:
            if i not in answer:
                    answer.append(i)
            b = b//i
            a = a//i
        else:
            i +=1
    # 기약분수 분모의 약수
    j = 2
    num = []
    while j<=b:
        if b%j==0 or b%j==5:
            if j not in num:
                num.append(j)
            b = b//j
        else: j+=1
    if len(num)==0: # 분자가 더 클 때
        return 1
    elif len(num)==2:
        if (num[0]==2) and (num[1]==5):
            return 1
        else:
            return 2
    elif len(num)==1:
        if (num[0]==2):
            return 1
        elif (num[0]==5):
            return 1
        else:
            return 2
    else:
        return 2

    