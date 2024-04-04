def solution(brown, yellow):
    answer = []
    number = brown+yellow
    
    for i in range(1, number):
        if number%i==0:
            if i>=(number//i):
                answer.append([i,number//i])
    
    for array in answer:
        if (array[0]-2)*(array[1]-2)==yellow:
            return array
    