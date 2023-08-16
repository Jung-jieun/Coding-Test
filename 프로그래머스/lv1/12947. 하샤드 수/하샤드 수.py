def solution(x):
    x = str(x)
    num = []
    for i in range(0, len(x)):
        num.append(int(x[i]))
    if int(x)%sum(num)==0:
        answer = True
    else:
        answer = False
    return answer