def solution(numlist, n):
    answer = []
    for i in numlist:
        answer.append(i-n)
    num = []
    for j in sorted(answer[:], key=lambda x:(abs(x),-x)):
        num.append(numlist[answer.index(j)])
    return num
