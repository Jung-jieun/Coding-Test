def solution(food):
    num1 = ''
    for i in range(1, len(food)):
        num1 += (food[i]//2)*str(i)
    
    return num1 + '0' + num1[::-1]