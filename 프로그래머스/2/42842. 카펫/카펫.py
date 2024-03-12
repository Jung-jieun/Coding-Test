def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, total+1):
        if total%i==0:
            j = total//i
            if (i>=j) and (i-2)*(j-2) == yellow:
                return [i, j]