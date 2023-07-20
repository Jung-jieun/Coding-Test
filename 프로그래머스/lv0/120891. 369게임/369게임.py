def solution(order):
    answer = []
    num = []
    for i in str(order):
        answer.append(int(i))
    for j in answer:
        if (j//3!=0) & (j%3==0):
            num.append(j)   
    return len(num)
        