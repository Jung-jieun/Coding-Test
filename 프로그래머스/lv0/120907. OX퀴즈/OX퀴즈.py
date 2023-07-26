def solution(quiz):
    answer = []
    for i in quiz:
        equ = i.split(" ")
        if equ[1] == "+":
            result = int(equ[0]) + int(equ[2])
        else:
            result = int(equ[0]) - int(equ[2])
        if int(equ[-1])==result:
            answer.append("O")
        else:
            answer.append("X")
    return answer