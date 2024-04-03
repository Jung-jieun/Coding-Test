def solution(answers):
    result = []
    student_1 = [1,2,3,4,5]
    student_2 = [2,1,2,3,2,4,2,5]
    student_3 = [3,3,1,1,2,2,4,4,5,5]
    
    num_1 = 0
    num_2 = 0
    num_3 = 0

    for idx, answer in enumerate(answers):
        if answer == student_1[idx%5]:
            num_1 += 1
        if answer == student_2[idx%8]:
            num_2 += 1
        if answer == student_3[idx%10]:
            num_3 += 1
            
    result.append(num_1)
    result.append(num_2)
    result.append(num_3)
    
    winner = []
    for student, number in enumerate(result):
        if number == max(result):
            winner.append(student+1)
    return winner