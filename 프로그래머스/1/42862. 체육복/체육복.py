def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    new_lost = [i for i in lost if i not in reserve]
    new_reserve = [i for i in reserve if i not in lost]
    
    for student in new_reserve:
        
        if student-1 in new_lost:
            new_lost.remove(student-1)
        elif student+1 in new_lost:
            new_lost.remove(student+1)
    
    return n-len(new_lost)