def solution(answers):
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    num1=num2=num3 = 0
    for i, answer in enumerate(answers):
        if student1[i % len(student1)] == answer:
            num1 += 1
        if student2[i % len(student2)] == answer:
            num2 += 1
        if student3[i % len(student3)] == answer:
            num3 += 1
    num = [num1, num2, num3]
    student = []
    for j in range(3):
        if num[j]==max(num):
            student.append(j+1)
    return student