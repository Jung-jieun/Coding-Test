def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow+1):
        if yellow%i == 0:
            x = yellow/i
            y = i
            if 2*(x+y) + 4 == brown:
                return [x+2, y+2]